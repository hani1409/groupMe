from groupy import Client
from tokens import tokens

client = Client.from_token(tokens['groupme'])

groups = list(client.groups.list_all())
for group in groups:
    if group.name == 'SI2 Youth Group':
        print(group.name)
        groupId = group.data['group_id']
        break

youthGroup = client.groups.get(groupId)
print(youthGroup.get_membership())