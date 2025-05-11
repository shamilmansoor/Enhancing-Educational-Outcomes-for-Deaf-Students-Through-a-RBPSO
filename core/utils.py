from joblib import load
import pandas as pd

def predict_marks(student):
    try:
        # Load model
        model = load("final_model.pkl")

        # Define feature columns used for prediction
        columns = [
            "Age", "Sex", "Address", "HearingLoss", "SchoolSupport", "PaidClasses",
            "IA1", "IA2", "IA3", "NurseryAttendance", "InternetAccess",
            "StudyTime", "Extracurricular", "Absences"
        ]

        # Create input data from student object
        input_row = [
            student.age,
            student.sex,
            student.address,
            student.hearing_loss,
            student.school_support,
            student.paid_classes,
            student.ia1,
            student.ia2,
            student.ia3,
            student.nursery_attendance,
            student.internet_access,
            student.study_time,
            student.extracurricular,
            student.absences
        ]

        # Create DataFrame for input
        df_input = pd.DataFrame([input_row], columns=columns)

        # Apply label encoding to categorical features
        for col in df_input.select_dtypes(include=['object']).columns:
            df_input[col] = df_input[col].astype('category').cat.codes

        # Predict
        prediction = model.predict(df_input)
        return float(prediction[0])
    except Exception as e:
        print(f"Prediction error: {str(e)}")
        return 0.0 