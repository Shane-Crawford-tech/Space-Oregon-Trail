# imported libraries
from random import randint
import textwrap



# This list holds the encounters to be chosen.
encounter_list = []


# This is the Encounters class, which creates the encounters.
class Encounter:
  def __init__(self, type, name, description, number_of_options = 1):
    self.type = type
    self.name = name
    self.description = description
    self.number_of_options = number_of_options
    self.encounter_option_list = []
    self.dialogues_list = []
    self.chances_list = []
    self.items_list = []
    self.responses = []
    self.first_results = []
    self.second_results = []
    self.usable_names = []
    self.usable_results = []
    self.response_currency_changes = []
    self.response_health_changes = []
    self.first_result_currency_changes = []
    self.first_result_health_changes = []
    self.second_result_currency_changes = []
    self.second_result_health_changes = []
    self.usable_currency_changes = []
    encounter_list.append(self)
    
# These functions are the types of options that an encounter can have (what the player can choose).
  def Choices(self, type, description):
    text = type + " " + description
    self.encounter_option_list.append(text)
    if type == "[Dialogue]":
      self.dialogues_list.append(text)
    if type == "[Chance]":
      self.chances_list.append(text)
    if type == "[Item/Weaponry]":
      self.items_list.append(text)

  def Results(self, response = None, first_result = None, second_result = None, usable_name = None, usable_result = None, 
              response_currency_change = 0, response_health_change = 0, first_result_currency_change = 0, first_result_health_change = 0, second_result_currency_change = 0, second_result_health_change = 0, usable_currency_change = 0):
    if response != None:
      self.responses.append(response)
      self.response_currency_changes.append(response_currency_change)
      self.response_health_changes.append(response_health_change)
    elif first_result != None and second_result == None:
      self.first_results.append(first_result)
      self.first_result_currency_changes.append(first_result_currency_change)
      self.first_result_health_changes.append(first_result_health_change)
    elif first_result != None and second_result != None:
      self.first_results.append(first_result)
      self.first_result_currency_changes.append(first_result_currency_change)
      self.first_result_health_changes.append(first_result_health_change)
      self.second_results.append(second_result)
      self.second_result_currency_changes.append(second_result_currency_change)
      self.second_result_health_changes.append(second_result_health_change)
    elif usable_name != None:
      self.usable_names.append(usable_name)
      self.usable_results.append(usable_result)
      self.usable_currency_changes.append(usable_currency_change)
    
# This section is where encounters are initiated.
e1 = Encounter("Trade", "Example Shop", "This is a shop.", 1)
e1.Choices("[Exit]", "You can leave the shop with this button.")
e1.Choices("[Trade]", "You can initiate trade with this button.")

e2 = Encounter("Event", "Astreoids", textwrap.fill("""Your colony approaches an asteroid field. The only way to get to your
 destination on time is to go through. Alternatively, you could change route and go around. What do you choose?""", width=50), 4)
e2.Choices("[Exit]", "Decide to go a different route.")
e2.Choices("[Chance]", "Decide to go through it anyways.")
e2.Results(None, "You succeeded in making it through! What a lucky break.", textwrap.fill("""Unfortunately, though you 
made it through the field, your ship took damage as a result, and some crew were lost.""", width=50), None, None, 0, 0, 0, 0, 0, -30)
e2.Choices("[Item/Weaponry]", "Fire away at the asteroids to clear a path.")
e2.Results(None, None, None, "Laser Cannons", "Firing your laser cannons, your ship blasts a clear path through the asteroids, making it out cleanly.")
e2.Choices("[Item/Weaponry]", "Overcharge the ship's reactor, giving it enough power to get through quick and unscathed.")
e2.Results(None, None, None, textwrap.fill("""Extra Reactor Core", "The core allowed for yoiur ship to get enough power 
           to charge through the field. Before you knew it, the ship was clear through.""",width=50))

e3 = Encounter("Ship-based", "Yearly Celebration", textwrap.fill("""As you do yearly, your colony hosts the anneversary of the Space Warlord's death.
This time, however, it seems the colony wants to have a massive feast. Will you keep the celebration modest, or go all out?""", width=50), 2)
e3.Choices("[Dialogue]", "Allow a feast to be had! The more food the merrier, as they say.")
e3.Results("Though it was a bit costly, the colony appriciates it. It seems the colony even grew as a result.", None, None, None, None, -50, 10)
e3.Choices("[Dialogue]", "Keep things modest. You will all need to keep supplies for the journey ahead.")
e3.Results("It was a small celebration, one that wouldn't hurt the colony in any way. Though that's not to say some people weren't annoyed.")

e4 = Encounter("Event", "Abandoned Vessel", textwrap.fill("""As your ship charts its course, you come across an 
abandoned fleet of vessels which don't appear to have been picked clean. Valuable loot could be found here.""", width=50), 3)
e4.Choices("[Exit]", "Continue past the fleet. Not worth risking your lives for.")
e4.Choices("[Chance]", "Choose to explore the vessels.")
e4.Results(None, textwrap.fill("""Upon further inspection, the ship appeared to be infected from some virus. The crew, however, 
           managed to fight their way through without any losses. They even found plenty of loot!, 
          Upon entry, the crew was ambushed by the infected remains of the fleet's previous inhabitants, leading to heavy casualties.""", width=50), None, None, 0, 0, 100, 0, 0, -60)
e4.Choices("[Item/Weaponry]", "Using your acquired long range radio, you radio the nearest fleet to inform them of the wreckage.")
e4.Results(None, None, None, "Long-Range Radio", textwrap.fill("""A salvage and containment crew were contacted, upon which your colony 
           was rewarded for the information. They should be able to handle things on their own.""", width=50), 0, 0, 0, 0, 0, 0, 400)

e5 = Encounter("Battle", "Bandit Fleet", textwrap.fill("""Your colony comes across a group of bandit ships on its travels. 
               They radio over, 'Give us all of your valuables and gold, or we will destroy that puny ship of yours-'. What is your response?""", width=50), 5)
e5.Choices("[Dialogue]", "Uhm....who are you, exactly?")
e5.Results(textwrap.fill("""....are you stupid? Do you really not know what a robbery is? Fucking colonists these days. 
           We  are  taking  your  stuff  or  killing  you  all. Got it now?""", width=50))
e5.Choices("[Give In]", textwrap.fill("""You conceide, allowing the bandits to dock aboard the ship to get 
           whatever they want. They don't hurt anyone, but you are now mostly broke and resourceless.""", width=50))
e5.Choices("[Chance]", "You attempt to persuade the bandits to let you go.")
e5.Results(None, textwrap.fill("""*a sigh can be heard over the radio*  'Okay, you know what? I don't have 
           time to deal with this today. Consider this your lucky break.' They end up leaving your ship alone, for the time being.", 
                 "'HAH! Seriously?! You think we would let you off that easy? Boys, prepare to blast this junk outta my face.' You 
           take signifigant casualties from the sudden barrage of fire, and are boarded afterwards.""", width=50), None, None, 0, 0, 0, 0, -1000, -600)
e5.Choices("[Item/Weaponry]", "Your obvious firepower makes you wonder why they even attempted this.")
e5.Results(None, None, None, textwrap.fill("""Heavy Rocket Pods", "*some voices can be heard in the background* 'Ah, 
           right....yes....really? Fuck....alright, you all get to live another day. But next time, next time....be prepared.' The bandits leave your ship alone.""", width=50))
e5.Choices("[Battle]", "No one attempts to attack your colony without punishment. To your stations!")



# This section chooses the encounter to display
random_number = randint(0, len(encounter_list)-1)
chosen_encounter = encounter_list[random_number]

shop = [e1]
peaceful = [e3]
event = [e2, e4]
hostile = [e5]

