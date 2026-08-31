import gradio as gr

import SimplePrompts


def greet(prompt, intensity, file):
            return SimplePrompts.promptEval(prompt, file[0],file[1],file[2])

demo = gr.Interface(
    fn=greet,
    inputs=[gr.TextArea(label="Prompt"), "slider",gr.FileExplorer(root_dir="./",label="Datei auswählen")],
    outputs=["text"],
    clear_btn="Zurücksetzen",
    submit_btn="Absenden"
)

demo.launch(share=True)