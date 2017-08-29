# from django.http import HttpResponse
# from channels.handler import AsgiHandler
# import json
# # def http_consumer(message):
# #     # Make standard HTTP response - access ASGI path attribute directly
# #     response = HttpResponse("Hello world! You asked for %s" % message.content['path'])
# #     # Encode that response into message format (ASGI)
# #     for chunk in AsgiHandler.encode_response(response):
# #         message.reply_channel.send(chunk

# def ws_message(message):
#     # ASGI WebSocket packet-received and send-packet message types
#     # both have a "text" key for their textual data.
#     message.reply_channel.send({
#         "text": message.content['text'],
#     })

# from channels import Group
# from channels.sessions import channel_session
# from urllib.parse import parse_qs
# # Connected to websocket.connect
# def ws_add(message):
#     # Accept the incoming connection
#     message.reply_channel.send({"accept": True})
#     # Add them to the chat group
#     Group("chat").add(message.reply_channel)

# # Connected to websocket.disconnect
# def ws_disconnect(message):
#     Group("chat").discard(message.reply_channel)
# # @channel_session
# # def ws_connect(message,room_id):
# # 	print("hhhhhhhhhh")
# # 	# Add to the chat group
# # 	message.reply_channel.send({"accept": True})
# # 	# Parse the query string
# # 	params = parse_qs(message.content["query_string"])
# # 	if b"username" in params:
# # 		# Set the username in the session
# # 		message.channel_session["username"] = params[b"username"][0].decode("utf8")
# # 		# Add the user to the room_id group
# # 		print("connect ",room_id)
# # 		Group("chat-%s" % room_id).add(message.reply_channel)
# # 	else:
# # 		# Close the connection.
# # 		message.reply_channel.send({"close": True})

# # # Connected to websocket.receive
# # @channel_session
# # def ws_message(message, room_id):
# # 	print("ggggg")
# # 	print("message ",room_id)
# # 	Group("chat-%s" % room_id).send({
# # 		"text": json.dumps({
# # 			"text": message["text"],
# # 			"username": message.channel_session["username"],
# # 		}),
# # 	})

# # # Connected to websocket.disconnect
# # @channel_session
# # def ws_disconnect(message, room_id):
# # 	print("hhhhhhhhhh")
# # 	print("disconnect ",room_id)
# # 	Group("chat-%s" % room_id).discard(message.reply_channel)

# from channels import Group

# # Connected to websocket.connect
# def ws_add(message):
# 	# Accept the connection

# 	print("in add")
# 	message.reply_channel.send({"accept": True})
# 	# Add to the chat group
# 	Group("chat").add(message.reply_channel)

# # Connected to websocket.receive
# def ws_message(message):
# 	print("in message")
# 	Group("chat").send({
# 		"text": "[user] %s" % message.content['text'],
# 	})

# # Connected to websocket.disconnect
# def ws_disconnect(message):
# 	print("in disconr")
# 	Group("chat").discard(message.reply_channel)


# import json
# from channels import Group
# from channels.sessions import channel_session
# from urllib.parse import parse_qs

# # Connected to websocket.connect
# @channel_session
# def ws_connect(message, room_id):
# 	# Accept connection
# 	print(room_id)
# 	message.reply_channel.send({"accept": True})
# 	# Parse the query string
# 	params = parse_qs(message.content["query_string"])
# 	if b"username" in params:
# 		# Set the username in the session
# 		print("user found")
# 		message.channel_session["username"] = params[b"username"][0].decode("utf8")
# 		# Add the user to the room_id group
# 		Group("chat-%s" % room_id).add(message.reply_channel)
# 	else:
# 		# Close the connection.
# 		print("not found user")
# 		message.reply_channel.send({"close": True})

# # Connected to websocket.receive
# @channel_session
# def ws_message(message, room_id):
# 	print("in mess")
# 	Group("chat-%s" % room_id).send({
# 		"text": json.dumps({
# 			"text": message["text"],
# 			"username": message.channel_session["username"],
# 		}),
# 	})

# # Connected to websocket.disconnect
# @channel_session
# def ws_disconnect(message, room_id):
# 	print("in disconnect")
# 	Group("chat-%s" % room_id).discard(message.reply_channel)



import json
from channels import Channel, Group
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http
from .models import Message,Room

# Connected to websocket.connect
@channel_session_user_from_http
def ws_connect(message,room_id):
	# Accept connection
	print("in connect")
	message.reply_channel.send({"accept": True})
	# Add them to the right group
	Group("chat-%s" % room_id).add(message.reply_channel)

# Connected to websocket.receive
@channel_session_user
def ws_message(message,room_id):
	print("in mess")
	Group("chat-%s" % room_id).send({
		"text": json.dumps(
			{
				"textMessage" : message["text"],
				"sender":message.user.username,
			}
			),

	})
	room = Room.objects.get(pk=room_id);
	user = message.user
	message_obj = Message.objects.create(title=message["text"],room=room,user=user)

# Connected to websocket.disconnect
@channel_session_user
def ws_disconnect(message,room_id):
	print("in discon")
	Group("chat-%s" % room_id).discard(message.reply_channel)