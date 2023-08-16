from .models import Items, Comments
import requests
import time

def get_data(index):
    url = requests.get(
        f'https://hacker-news.firebaseio.com/v0/item/{index}.json?print=pretty'
    )
    return url.json()
def GetComments(kids,item_id):
    comments = Comments()
    for kid in kids:
        comment_data = get_data(kid)
        comments.id = comment_data['id']
        comments.by = comment_data.get('by','')
        comments.type = comment_data['type']
        comments.text = comment_data.get('text','')
        comments.item = Items.objects.get(id=item_id)
        comments.deleted = comment_data.get('deleted',False)
        comments.dead = comment_data.get('dead',False)
        comments.save()
        if children := comment_data.get('kids'):
            GetChildComments(children,item_id, comments.id)
            print('complete saving')
        comments.save()
    
def GetChildComments(children, item_id, comment_id):
    comments = Comments()
    for child in children:
        comment_data = get_data(child)
        comments.id = comment_data['id']
        comments.by = comment_data.get('by','')
        comments.type = comment_data['type']
        comments.text = comment_data.get('text','')
        comments.item = Items.objects.get(id=item_id)
        comments.parent = Comments.objects.get(id=comment_id)
        comments.deleted = comment_data.get('deleted',False)
        comments.dead = comment_data.get('dead',False)
        comments.save()



def GetStories(stories):
    items = Items()
    for i in stories:
        story = get_data(i) # this contains all items or events.

        try: 
            items.id = story.get('id','')
            items.by = story.get('by','')
            items.type = story['type']
            items.title = story.get('title')
            items.url = story.get('url','')
            items.descendants = story.get('descendants','')
            items.dead = story.get('dead',False)
            items.deleted = story.get('deleted', False)
            items.save()
            if kids := story.get('kids'):
                GetComments(kids,items.id)
            items.save()
        except KeyError as err:
            print(err)


def updateStories(keyword):
    #update the items table
    story = requests.get( f'https://hacker-news.firebaseio.com/v0/{keyword}.json?print=pretty')
    GetStories(story.json()) 
    # contains only the recent events

def updateNewStories():
    updateStories('newstories')

# def updateTopstories()
#     updateStories('topstories')


# def get_comments():
#     items = Items.objects.filter(type='comment')
    
#     print(len(items))
#     for i in items:
#         comments = Comments.objects.create(post=i)

#     return comments

