from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


def test_history_delete(app_test):
    # criar no db user admin com token
    UserModel(
        {"name": "John Dall", "level": "admin", "token": "mytoken_987"}
    ).save()
    # criação de registro a ser deletado
    HistoryModel(
        {
            "text-to-translate": "Do you love music?",
            "translate-from": "en",
            "translate-to": "pt",
        }
    ).save()

    # busca id do registro a ser deletado
    history_id = HistoryModel.find_one({"translate_from": "en"}).data[
        "_id"
    ]

    # implementar requisição de deleção do registro
    response = app_test.delete(
        f"/admin/history/{history_id}",
        headers={"Authorization": "mytoken_987", "User": "John Dall"},
    )
    assert response.status_code == 204
