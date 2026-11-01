import os
import requests
import gradio as gr

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")


def interpret_video(video_path: str):
    if video_path is None:
        yield "", "Please upload a video first."
        return

    yield "", "Sending video to backend..."

    try:
        with open(video_path, "rb") as f:
            filename = os.path.basename(video_path)
            size_mb = os.path.getsize(video_path) / (1024 * 1024)
            yield "", f"Uploading {filename} ({size_mb:.1f} MB) — waiting for Gemini..."

            response = requests.post(
                f"{BACKEND_URL}/predict",
                files={"video": (filename, f, "video/mp4")},
                timeout=180,
            )

        if response.status_code == 200:
            interpretation = response.json()["interpretation"]
            yield interpretation, "Done"
        else:
            yield "", f"Backend error {response.status_code}: {response.text}"

    except requests.exceptions.ConnectionError:
        yield "", "Cannot reach backend. Make sure it is running on port 8000."
    except requests.exceptions.Timeout:
        yield "", "Request timed out. Gemini may still be processing — try a shorter video."
    except Exception as e:
        yield "", f"Unexpected error: {e}"


with gr.Blocks(title="ISL Interpreter", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# ISL Sign Language Interpreter")
    gr.Markdown("Upload a short video (10–15 seconds) of someone signing in Indian Sign Language.")

    with gr.Row():
        with gr.Column(scale=1):
            video_input = gr.Video(label="Input Video", sources=["upload"])
            submit_btn = gr.Button("Interpret", variant="primary")

        with gr.Column(scale=1):
            output_text = gr.Textbox(
                label="Interpretation",
                lines=6,
                placeholder="The ISL interpretation will appear here...",
                interactive=False,
            )
            status_text = gr.Textbox(label="Status", interactive=False, max_lines=1)

    submit_btn.click(
        fn=interpret_video,
        inputs=[video_input],
        outputs=[output_text, status_text],
    )

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860)


