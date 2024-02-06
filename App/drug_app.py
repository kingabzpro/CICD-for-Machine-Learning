import gradio as gr
import skops.io as sio

pipe = sio.load("./Model/drug_pipeline.skops", trusted=True)


def classifier(Age, Sex, BP, Cholesterol, Na_to_K):
    """
    This function takes input features Age, Sex, BP, Cholesterol, and Na_to_K,
    and uses a sklearn pipeline to make a prediction on the glass label.

    Args:
    Age (float): The age of the patient
    Sex (str): The sex of the patient (M or F)
    BP (str): The blood pressure of the patient (HIGH, NORMAL, or LOW)
    Cholesterol (str): The cholesterol level of the patient (HIGH or NORMAL)
    Na_to_K (float): The ratio of sodium to potassium in the patient's blood

    Returns:
    str: A string with the predicted drug label
    """
    pred_drug = pipe.predict([[Age, Sex, BP, Cholesterol, Na_to_K]])[0]
    label = f"Predicted Drug label: **{pred_drug}**"
    return label


inputs = [
    gr.Slider(15, 74, step=1, label="Age"),
    gr.Radio(["M", "F"], label="Sex"),
    gr.Radio(["HIGH", "LOW", "NORMAL"], label="Blood Pressure"),
    gr.Radio(["HIGH", "NORMAL"], label="Cholesterol"),
    gr.Slider(6.2, 38.2, step=0.1, label="Na_to_K"),
]
outputs = [gr.Label(num_top_classes=5)]

examples = [
    [30, "M", "HIGH", "NORMAL", 15.4],
    [35, "F", "LOW", "NORMAL", 8],
    [50, "M", "HIGH", "HIGH", 34],
]


title = "Drug Classification"
description = "Enter the details to correctly identify Drug type?"

gr.Interface(
    fn=classifier,
    inputs=inputs,
    outputs=outputs,
    examples=examples,
    title=title,
    description=description,
).launch()
