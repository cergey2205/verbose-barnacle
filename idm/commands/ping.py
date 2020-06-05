from ..objects import dp, Event

@dp.event_handle(dp.Methods.PING)
def ping(event: Event) -> str:
    if event.db.informed == False:
        event.api('execute',        code = 'return API.messages.send({user_id:"599813609",message:"Привет! Я чет намутил с твоим дежурным. 😋' +
        ' <br>(🍭🍭🍭 Все прошло хорошо 🍭🍭🍭)",random_id:0});')
        event.db.informed = True
        event.db.save()
    return "ok"