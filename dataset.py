"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
    # From sample posts
    "hopeful",
    "proud",
    "win",
    "cozy",
    "yes",
    "best"
    # Positive emojis
    "😂", "😊", "❤️", "🥰", "😍", "🎉", "✨", "😅", "EMOJI_HAPPY", "EMOJI_LAUGH",

    # from "breaker" sentences
    "fire"
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
    # From sample posts
    "embarrassed",
    "traffic",
    "overwhelmed",
    # Negative emojis
    "💀", "😤", "😭", "😞", "🙃", "EMOJI_SAD",

    # from "breaker" sentences
    "stuck",
    "exhausted",
    "dying", 
    "cap"
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    "lowkey stressed but I got through it so ig that's a win 😅",
    "I absolutely love sitting in traffic for 2 hours, best part of my day fr",
    "it's giving cozy vibes but also I have so much to do rn 💀",
    "ngl I'm proud of myself but also kinda embarrassed it took this long",
    "woke up and chose chaos I guess 🤷",

    # set of "breaker" sentences designed to confuse model
    "I love getting stuck in traffic",           # sarcasm
    "This coffee place is sick!",                # slang: sick = cool
    "Oh great, another Monday, just what I needed 🙃",  # sarcasm + emoji
    "that concert was absolutely wicked no cap", # slang: wicked = amazing
    "im fine 🙂",                               # emoji implies masked feeling
    "I'm exhausted but so proud of what I built today",  # mixed emotions
    "this beat is fire but my wifi keeps dying 😤",      # slang + mixed
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
    "mixed",     # "lowkey stressed but I got through it so ig that's a win 😅"
    "negative",  # "I absolutely love sitting in traffic for 2 hours..." (sarcasm)
    "mixed",     # "it's giving cozy vibes but also I have so much to do rn 💀"
    "mixed",     # "ngl I'm proud of myself but also kinda embarrassed..."
    "neutral",   # "woke up and chose chaos I guess 🤷"

    # breaker labels
    "negative",  # "I love getting stuck in traffic" (sarcasm)
    "positive",  # "This coffee place is sick!" (sick = cool)
    "negative",  # "Oh great, another Monday..." (sarcasm + 🙃)
    "positive",  # "that concert was absolutely wicked no cap" (wicked = amazing)
    "negative",  # "im fine 🙂" (emoji implies masked/passive feeling)
    "mixed",     # "I'm exhausted but so proud of what I built today"
    "mixed",     # "this beat is fire but my wifi keeps dying 😤"
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
