import mlflow

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(data, *args, **kwargs):
    #mlflow.set_tracking_uri("sqlite:////home/mlflow/mlflow.db")
    mlflow.set_experiment("experiment_001")

    with mlflow.start_run():
        mlflow.set_tag('developer', 'Maruf')

        mlflow.log_artifact(data[0], artifact_path='preprocessor')
        mlflow.sklearn.log_model(data[1], artifact_path='artifacts')
