from ..objects import dp, Event
from .. import utils
from vkapi import VkApiResponseException

@dp.event_handle(dp.Methods.ADD_USER)
def add_user(event: Event) -> str:
    user = event.api('users.get', user_ids=event.obj['user_id'])[0]
    message = f"💚 Добавляю [id{user['id']}|{user['first_name']} {user['last_name']}]"

    message_id = utils.new_message(event.api, event.chat.peer_id, message=message)

    try:
        event.api('messages.addChatUser', chat_id=event.chat.id, user_id=user['id'])
        message = f"✅ Пользователь [id{user['id']}|{user['first_name']} {user['last_name']}] в чатике 😎"
    except VkApiResponseException as e:
        if e.error_code == 15:
            message = f"❗ Не удалось добавить [id{user['id']}|{user['first_name']} {user['last_name']}].\nНе в моих друзьях или уже в беседе 🤷‍♀"
        else:
            message = f"❗ Не удалось добавить [id{user['id']}|{user['first_name']} {user['last_name']}].\nОшибка ВК.\n{e.error_msg}"
    except:
        message = f"❗ Не удалось добавить [id{user['id']}|{user['first_name']} {user['last_name']}].\nПроизошла неизвестная ошибка." 
    utils.edit_message(event.api, event.chat.peer_id, message_id, message=message)
    return "ok"
