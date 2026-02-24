{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a328a03b-ae09-44b0-a187-02692f24386c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import joblib\n",
    "\n",
    "MODEL_PATH = \"../models/rf_pipeline.pkl\"\n",
    "\n",
    "\n",
    "def predict(input_path):\n",
    "\n",
    "    model = joblib.load(MODEL_PATH)\n",
    "\n",
    "    new_data = pd.read_excel(input_path)\n",
    "\n",
    "    predictions = model.predict(new_data)\n",
    "\n",
    "    return predictions\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    preds = predict(\"../data/sample_input.xlsx\")\n",
    "    print(preds)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (ML)",
   "language": "python",
   "name": "ml"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
