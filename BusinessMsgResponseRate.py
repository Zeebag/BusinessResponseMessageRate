import math
def response_rate(bizOwnerId, allMessages):
    # allMessages is a list of mesasges class
    # bizOwnderId id representing bizOwner
    conversation_dict = dict()
    for message in allMessages:
        if message['sender'] == bizOwnerId: # the messege from the business owner which belong to a conversation
            conv_id =  message['conversationId']
            if conv_id in conversation_dict:
                conversation_dict[conv_id] += 1
            else:
                conversation_dict[conv_id] = 1

    # number of conversation where business owner wrote >= 1 message
    counter = conversation_dict.values()
    counter = math.fsum(counter)
    print(counter)

    # total unique  number of conversation where business owner is involved
    conversation_dict_total = dict()
    for message_total in allMessages:
        if ((message_total['sender'] == bizOwnerId) or (message_total['recipient'] == bizOwnerId)):
            conv_id_total =  message_total['conversationId']
            if conv_id_total in conversation_dict_total:
                conversation_dict_total[conv_id_total] += 1
            else:
                conversation_dict_total[conv_id_total] = 1

    total = conversation_dict_total.values()
    total = math.fsum(total)
    print("##############")
    print("total")
    print(total)
    print("##############")
    if total == 0:
        return 0
    else:
        resp_rate = math.floor((counter/total) * 100 )
        return resp_rate

##################### sample input #####################
allMessages = [
    {
        'sender': 2,
        'recipient': 3,
        'conversationId': 56
    },
    {
        'sender': 6,
        'recipient': 3,
        'conversationId': 56
    },
    {
        'sender': 7,
        'recipient': 2,
        'conversationId': 87
    },
    {
        'sender': 2,
        'recipient': 3,
        'conversationId': 56
    },
    {
        'sender': 2,
        'recipient': 7,
        'conversationId': 87
     },
    {
        'sender': 2,
        'recipient': 3,
        'conversationId': 87
    },
    {
        'sender': 2,
        'recipient': 7,
        'conversationId': 60
    },
    {
        'sender': 7,
        'recipient': 3,
        'conversationId': 60
     },
    {
        'sender': 7,
        'recipient': 3,
        'conversationId': 56
     },
    {
        'sender': 4,
        'recipient': 3,
        'conversationId': 56
    },
    {
        'sender': 4,
        'recipient': 3,
        'conversationId': 56
    },
    {
        'sender': 2,
        'recipient': 3,
        'conversationId': 56
     },
    {
        'sender': 7,
        'recipient': 2,
        'conversationId': 60
     },
    {
        'sender': 7,
        'recipient': 3,
        'conversationId': 60
     }
    
]
print(response_rate(7, allMessages))

