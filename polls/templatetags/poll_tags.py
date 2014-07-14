from django import template
register = template.Library()

def get_percent(option):
  poll = option.poll

  votes = 0
  for opt in poll.option_set.all():
    votes += opt.hits

  return option.hits * 100.0 / votes

register.filter('get_percent', get_percent)
