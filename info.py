# import pickle

# with open("stresslevel.pkl", "rb") as file:
#     model = pickle.load(file)
    
# # Check scikit-learn version used for this model
# if hasattr(model, "_sklearn_version"):
#     print(f"Model was trained with scikit-learn version: {model._sklearn_version}")
# else:
#     print("No version information found in the pickle file.")

from app import app, db

with app.app_context():
    print(db.engine.url.database)