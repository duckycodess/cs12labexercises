from oj import Comment
from typing import Sequence

def winners(comments: Sequence[Comment], threshold: int) -> list[str]:

    def collect_comments(comment: Comment, all_comments: list[Comment]) -> None:
        all_comments.append(comment)
        for reply in comment.responses:
            collect_comments(reply, all_comments)
    
    all_comments: list[Comment] = []

    for comment in comments:
        collect_comments(comment, all_comments)
        
    filtered_comments = [here.text for here in all_comments if here.upvote_count > threshold]
    filtered_comments.sort(key=lambda c: (len(c), c))

    return sorted(filtered_comments[-3:])

