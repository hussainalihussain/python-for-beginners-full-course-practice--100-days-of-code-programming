import asyncio
from desktop_notifier import DesktopNotifier

async def notify(title, message=None):
  notifier = DesktopNotifier()

  if message == None:
     message = title

  await notifier.send(title=title, message=message)
