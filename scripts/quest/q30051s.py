# id 30051 ([Theme Dungeon] The Straight-Faced Princess), field 106030000
sm.setSpeakerID(1302000) # Mushking
sm.setParam(32)
sm.setColor(1)
sm.sendNext("Welcome to Mushroom Castle, stranger.\r\nI appreciate you coming all the way here. I'm sure Violetta's portrait was more than enough motivation, of course.")
sm.setParam(56)
sm.sendSay("...Her looks are much more shocking in person.")
sm.setParam(32)
sm.sendSay("Yes, Violetta's devilish charms works on anybody, regardless of gender. I'm certain you're wishing to be a candidate for her #r#ehand in marriage#k#n!")
sm.setParam(56)
sm.sendSay("Her spouse? Not at all. (You give your most serious face)")
sm.setParam(32)
sm.sendSay("As you can see, a competition is being held here. The #rVioletta's Smile Competition#k, to be exact. My daughter has never smiled for us in her life, you see. I feel like I have failed as a father... But I also think it's Violetta trying to discourage the unworthy masses, lovesick with her beauty...")
res = sm.sendAskAccept("So I have decided to give the throne to whosoever can make Violetta smile, and become her spouse. It's the only sensible way to decide the kingdom's fate. Mushrooms only, I'm afraid but you can visit with the princess if you like. Go ahead.")
sm.startQuest(parentID)
sm.sendSayOkay("Try not to fall in love with her. I guess it can't be helped, though.")