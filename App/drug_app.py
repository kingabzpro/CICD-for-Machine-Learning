import gradio as gr
import skops.io as sio

pipe = sio.load("./Model/drug_pipeline.skops", trusted=True)


def classifier(Age, Sex, BP, Cholesterol, Na_to_K):
    pred_glass = pipe.predict([[Age, Sex, BP, Cholesterol, Na_to_K]])[0]
    label = f"Predicted Glass label: **{pred_glass}**"
    return label


inputs = [
    gr.Slider(15, 74, step=1, label="Age", default=30),
    gr.Radio(["M", "F"], label="Sex", default="F"),
    gr.Radio(["HIGH", "LOW", "NORMAL"], label="Blood Pressure", default="LOW"),
    gr.Radio(["HIGH", "NORMAL"], label="Cholesterol", default="NORMAL"),
    gr.Slider(6.2, 38.2, step=0.1, label="Na_to_K", default=13.2),
]
outputs = [gr.Label(num_top_classes=5)]

title = "Drug Classification"
description = "Enter the details to correctly identify Drug type?"

gr.Interface(
    fn=classifier,
    inputs=inputs,
    outputs=outputs,
    title=title,
    description=description,
).launch()
