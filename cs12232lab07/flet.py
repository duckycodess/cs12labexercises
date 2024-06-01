import flet as ft

from cs12232lab07lib import authenticate, Session
from cs12232lab07lib.project_types import ChatMessage


async def login() -> Session:
    print('Enter name: ')
    name = input()  # Must have no arguments; Flet issue
    print('Enter password: ')
    password = input()  # Must have no arguments; Flet issue

    try:
        session = await authenticate(name, password, 'ws://oj.dcs.upd.edu.ph:7777/ws')
    except ValueError:
        print('Invalid credentials!')
        exit(1)

    return session


async def app_main(page: ft.Page):
    session = await login()
    chat_history = []

    def display_msg(chat: ChatMessage):
        if not dm_on.value:
            message = ft.Text(value=f"{chat.src}: {chat.msg}")
            history.controls.append(message)
            page.update()
        elif dm_on.value and receipent.value is not None:
            peeps = receipent.value.split(', ')
            for ppl in peeps:
                message = ft.Text(value=f'{chat.src} -> {ppl}: {chat.msg}')
                history.controls.append(message)
                page.update()

    async def send_message(_: ft.ControlEvent):
        nonlocal chat
        if message_box.value is not None and not dm_on.value:
            chat.append(ChatMessage(session.username, None, message_box.value))
            session.send_group_chat_message(message_box.value)
            message_box.value = ''

        elif message_box.value is not None and dm_on.value and receipent.value is not None:
            for ppl in receipent.value.split(', '):
                session.send_direct_message(message_box.value, ppl)
                chat.append(ChatMessage(session.username, ppl, message_box.value))
            message_box.value = ''


    chat: list[ChatMessage] = []
    message_box = ft.TextField(label='Send a Message')
    send_button = ft.OutlinedButton(text='Send', on_click=send_message)
    row = ft.Row()
    dm_on = ft.Checkbox(label='DM?', value=False)
    receipent = ft.TextField(label='Recepient(s)')
    row.controls.append(dm_on)
    row.controls.append(receipent)
    history = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )
    search_row = ft.Row()
    search_row.controls.append(ft.TextField(label='Search...'))
    search_row.controls.append(ft.OutlinedButton(text='Search'))

    page.add(message_box)
    page.add(send_button)
    page.add(row)
    page.add(search_row)
    page.add(history)

    page.run_task(session.make_task(on_chat_received=display_msg))


def main():
    ft.app(app_main)


if __name__ == '__main__':
    main()
