# id 17647 ([Commerci Republic] The Fall of Captain Blood), field 865010001
sm.setSpeakerID(9390243) # Robed Lady
sm.setParam(32)
sm.setColor(1)
sm.sendNext("Everyone step back. I don't want anyone being swept out to sea.")
sm.lockInGameUI(True, True)
sm.forcedInput(0)
sm.showFieldEffect("Map/EffectBT.img/dawnveil1/Cut3_1", 0)
sm.sendDelay(2000)
sm.showFieldEffect("Map/EffectBT.img/dawnveil1/Cut3_2", 0)
sm.playSound("Sound/SoundEff.img/thunder3", 100)
sm.sendDelay(2000)
sm.lockInGameUI(False, True)
sm.setParam(57)
sm.sendNext("..........")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9390235) # Leon Daniella
sm.sendSay("..........")
sm.setParam(57)
sm.sendSay("Yikes... I wonder if they made it. ")
sm.setParam(37)
sm.sendSay("Umm... That seems unlikely.")
sm.setParam(57)
sm.sendSay("I almost feel bad for them now.")
sm.setParam(33)
sm.sendSay("Now, to discuss my payment.")
sm.completeQuestNoCheck(parentID)
sm.createQuestWithQRValue(18418, "B=33276")