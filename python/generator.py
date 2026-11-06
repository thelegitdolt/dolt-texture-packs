from PIL import Image
import paths


MODID_savepath = lambda modid: f"{paths.desktop}/Minecraft Modpacks/1.20 Doltpack Dev/resourcepacks/FusionDyeDepotCTM/assets/{modid}"
colors = ["verdant", "teal", "slate", "tan", "rose", "navy", "olive", "mint", "maroon", "indigo", "ginger", "forest", "beige", "coral", "aqua", "amber"]
source = f"{paths.desktop}/code/MidnightTiggersCTM/fusion/assets/minecraft/models/block/mt-ct/"

pane_list = ["black_glass_pane_straight",
"black_glass_pane_side_west",
"black_glass_pane_side_south",
"black_glass_pane_side_north",
"black_glass_pane_side_east",
"black_glass_pane_post",
"black_glass_pane_noside_west",
"black_glass_pane_noside_south",
"black_glass_pane_noside_north",
"black_glass_pane_noside_east",
"black_glass_pane_end",
"black_glass_pane_corner"]

def do_pane_model(color, modid):
  for pane in pane_list:
    with open(source + pane + ".json", 'r') as file:
      filejson = file.read().replace("minecraft:black_stained_glass_pane", f"{modid}:{color}_glass_pane").replace("minecraft:block/mt-ct/black_stained_glass", f"{modid}:block/{color}_glass").replace("minecraft:block/black_stained_glass_pane_top", f"{modid}:block/{color}_glass_pane_top")
      newpane = pane.replace("black", color)
      with open(MODID_savepath(modid) + f"/models/block/{newpane}.json", 'w') as newfile:
        newfile.write(filejson)

def do_blockstates(color, modid):
  with open(MODID_savepath(modid) + f"/blockstates/{color}_glass_pane.json", 'w') as blockstatefile:
    blockstatefile.write(blockstate(color, modid))

def blockstate(color, modid):
  return """
{
  "multipart": [
    {
      "apply": {
        "model": "???:block/@@@_glass_pane_side_north"
      },
      "when": {
        "north": "true"
      }
    },
    {
      "apply": {
        "model": "???:block/@@@_glass_pane_side_east",
        "y": 90
      },
      "when": {
        "east": "true"
      }
    },
    {
      "apply": {
        "model": "???:block/@@@_glass_pane_side_south",
        "y": 180
      },
      "when": {
        "south": "true"
      }
    },
    {
      "apply": {
        "model": "???:block/@@@_glass_pane_side_west",
        "y": 270
      },
      "when": {
        "west": "true"
      }
    },
    {
      "apply": {
        "model": "???:block/@@@_glass_pane_noside_north"
      },
      "when": {
        "east": "true",
        "south": "false",
        "west": "true"
      }
    },
    {
      "apply": {
        "model": "???:block/@@@_glass_pane_noside_east",
        "y": 90
      },
      "when": {
        "north": "true",
        "south": "true",
        "west": "false"
      }
    },
    {
      "apply": {
        "model": "???:block/@@@_glass_pane_noside_south",
        "y": 180
      },
      "when": {
        "north": "false",
        "east": "true",
        "west": "true"
      }
    },
    {
      "apply": {
        "model": "???:block/@@@_glass_pane_noside_west",
        "y": 270
      },
      "when": {
        "north": "true",
        "east": "false",
        "south": "true"
      }
    },
    {
      "apply": {
        "model": "???:block/@@@_glass_pane_straight"
      },
      "when": {
        "north": "true",
        "west": "false"
      }
    },
    {
      "apply": {
        "model": "???:block/@@@_glass_pane_straight",
        "y": 90
      },
      "when": {
        "east": "true",
        "north": "false"
      }
    },
    {
      "apply": {
        "model": "???:block/@@@_glass_pane_straight"
      },
      "when": {
        "OR": [
          {
            "south": "true",
            "east": "false",
            "north": "false"
          },
          {
            "north": "true",
            "south": "true",
            "west": "true"
          }
        ]
      }
    },
    {
      "apply": {
        "model": "???:block/@@@_glass_pane_straight",
        "y": 90
      },
      "when": {
        "OR": [
          {
            "west": "true",
            "south": "false",
            "east": "false"
          },
          {
            "north": "true",
            "east": "true",
            "south": "false",
            "west": "true"
          }
        ]
      }
    },
    {
      "apply": {
        "model": "???:block/@@@_glass_pane_corner"
      },
      "when": {
        "north": "true",
        "east": "true",
        "south": "false",
        "west": "false"
      }
    },
    {
      "apply": {
        "model": "???:block/@@@_glass_pane_corner",
        "y": 90
      },
      "when": {
        "north": "false",
        "east": "true",
        "south": "true",
        "west": "false"
      }
    },
    {
      "apply": {
        "model": "???:block/@@@_glass_pane_corner",
        "y": 180
      },
      "when": {
        "north": "false",
        "east": "false",
        "south": "true",
        "west": "true"
      }
    },
    {
      "apply": {
        "model": "???:block/@@@_glass_pane_corner",
        "y": 270
      },
      "when": {
        "north": "true",
        "east": "false",
        "south": "false",
        "west": "true"
      }
    },
    {
      "apply": {
        "model": "???:block/@@@_glass_pane_end"
      },
      "when": {
        "north": "true",
        "east": "false",
        "south": "false",
        "west": "false"
      }
    },
    {
      "apply": {
        "model": "???:block/@@@_glass_pane_end",
        "y": 90
      },
      "when": {
        "north": "false",
        "east": "true",
        "south": "false",
        "west": "false"
      }
    },
    {
      "apply": {
        "model": "???:block/@@@_glass_pane_end",
        "y": 180
      },
      "when": {
        "north": "false",
        "east": "false",
        "south": "true",
        "west": "false"
      }
    },
    {
      "apply": {
        "model": "???:block/@@@_glass_pane_end",
        "y": 270
      },
      "when": {
        "north": "false",
        "east": "false",
        "south": "false",
        "west": "true"
      }
    },
    {
      "apply": {
        "model": "???:block/@@@_glass_pane_post"
      },
      "when": {
        "north": "false",
        "east": "false",
        "south": "false",
        "west": "false"
      }
    }
  ]
} 
""".replace("@@@", color).replace("???", modid)

def do_model(color, modid):
  return """{
  "loader": "fusion:model",
  "type": "connecting",
  "connections": {
    "all": {
      "type": "is_same_block"
    }
  },
  "parent": "minecraft:block/cube_all",
  "textures": {
    "all": "MODID:block/@@@_glass"
  }
}
""".replace("@@@", color).replace("MODID", modid)

def do_model_in_file(color, path=f"{MODID_savepath}/models/block/"):
  with open(path + color + "_glass.json", 'w') as file:
    file.write(do_model(color))


def do_image(color, modid):
  images = [Image.open(john_path(color) + str(i) + ".png") for i in range(5)]
  widths, heights = zip(*(i.size for i in images))

  total_width = sum(widths)
  max_height = max(heights)

  new_im = Image.new('RGBA', (total_width, max_height))

  x_offset = 0
  for im in images:
    new_im.paste(im, (x_offset,0))
    x_offset += im.size[0]

  new_im.save(f'{MODID_savepath(modid)}/textures/block/{color}_stained_glass.png')
  with open(f"{MODID_savepath(modid)}/textures/block/{color}_stained_glass.png.mcmeta", 'w') as file:
    file.write("""
{
  "fusion": {
    "type": "connecting",
    "render_type": "translucent",
    "layout": "pieced"
  }
}
    """)
if __name__ == "__main__":
  do_pane_model("arid", "atmospheric")
  do_blockstates("arid", "atmospheric")
