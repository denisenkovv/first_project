def prediction_to_answer(prediction, threshold=0.5):
    if prediction <= threshold:
        print("Yes")
    else: 
        print("No")