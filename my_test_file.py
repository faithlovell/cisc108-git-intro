# Some text in this file to push
# Fun fact: I draw/ write my smiley faces with pointy noses, like this: :^)

def example_function(branch_name: str) -> str:
    return "I am in branch: " + branch_name


print(example_function("branching-example"))


def create_conflict(name: str) -> str:
    return name + " just created a merge conflict!"


print(create_conflict("Faith"))
