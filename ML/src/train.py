{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "51061c13-7da1-4148-a1df-22de3fae58e8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# src/train.py\n",
    "\n",
    "import pandas as pd\n",
    "import joblib\n",
    "from sklearn.model_selection import train_test_split, cross_val_score\n",
    "from sklearn.metrics import r2_score\n",
    "\n",
    "from pipeline import build_pipeline\n",
    "\n",
    "\n",
    "DATA_PATH = \"data/Heavy_Machinery_Database.xlsx\"\n",
    "TARGET = \"Ton-kilometer fuel consumption L / km / t\"\n",
    "MODEL_OUTPUT = \"models/rf_pipeline.pkl\"\n",
    "\n",
    "\n",
    "def main():\n",
    "\n",
    "    # Load data\n",
    "    df = pd.read_excel(DATA_PATH)\n",
    "\n",
    "    X = df.drop(columns=[TARGET])\n",
    "    y = df[TARGET]\n",
    "\n",
    "    # Split\n",
    "    X_train, X_test, y_train, y_test = train_test_split(\n",
    "        X, y,\n",
    "        test_size=0.2,\n",
    "        random_state=42\n",
    "    )\n",
    "\n",
    "    # Build pipeline\n",
    "    model = build_pipeline()\n",
    "\n",
    "    # Train\n",
    "    model.fit(X_train, y_train)\n",
    "\n",
    "    # Evaluate\n",
    "    y_pred = model.predict(X_test)\n",
    "    print(\"Test R2:\", r2_score(y_test, y_pred))\n",
    "\n",
    "    # Cross validation\n",
    "    cv_scores = cross_val_score(model, X_train, y_train,\n",
    "                                cv=5, scoring=\"r2\")\n",
    "\n",
    "    print(\"CV R2 Mean:\", cv_scores.mean())\n",
    "    print(\"CV R2 Std:\", cv_scores.std())\n",
    "\n",
    "    # Save model\n",
    "    joblib.dump(model, MODEL_OUTPUT)\n",
    "    print(\"Model saved to:\", MODEL_OUTPUT)\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
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
