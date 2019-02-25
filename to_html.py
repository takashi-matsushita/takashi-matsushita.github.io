import io, os
from datetime import datetime

from jinja2 import Environment, FileSystemLoader


import tools
info = tools.getInformation()
loop = tools.getNavigation()
loop = tools.getConferences(loop)
loop = tools.getPublications(loop)
link = tools.getLinks()


THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def render(template):
  j2_env = Environment(loader=FileSystemLoader(THIS_DIR),
                       trim_blocks=True)
  j2_env.add_extension('jinja2.ext.loopcontrols')

  association = {
    "info": info,
    "loop": loop,
    "link": link,
  }

  return j2_env.get_template(template).render(association)


if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser()

  parser.add_argument("--input", dest="input", default=None, type=str, action="store", required=True, help="input file")
  parser.add_argument("--output", dest="output", default=None, type=str, action="store", help="output file")

  options = parser.parse_args()

  if not options.output:
    name = os.path.basename(options.input)
    name, ext = os.path.splitext(name)
    options.output = name + '.html'
    
  text = render(options.input)
  with io.open(options.output, "w") as fp:
    fp.write(text)
  
  print(THIS_DIR)
# eof
