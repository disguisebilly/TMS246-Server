# id 402090012 (null), field 402090012
sm.lockInGameUI(True, False)
sm.removeAdditionalEffect()
sm.spawnNpc(3001512, -700, 20)
sm.showNpcSpecialActionByTemplateId(3001512, "summon", 0)
sm.spawnNpc(3001513, -640, 20)
sm.showNpcSpecialActionByTemplateId(3001513, "summon", 0)
sm.spawnNpc(3001510, -470, 20)
sm.showNpcSpecialActionByTemplateId(3001510, "summon", 0)
sm.spawnNpc(3001509, -800, 20)
sm.showNpcSpecialActionByTemplateId(3001509, "summon", 0)
sm.moveNpcByTemplateId(3001510, False, 1500, 200)
sm.moveNpcByTemplateId(3001509, False, 1500, 200)
sm.moveNpcByTemplateId(3001512, False, 1500, 200)
sm.moveNpcByTemplateId(3001513, False, 1500, 200)
sm.forcedMove(False, 1500)
sm.blind(True, 150, 0, 0, 0, 1300)
sm.sendDelay(1000)
sm.sayMonologue("My memory keeps getting clearer.", 0)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/D/Male/1", 100)
sm.sayMonologue("And as it does, all of my old feelings come rushing back.", 0)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/D/Male/2", 100)
sm.sayMonologue("\r\nEverything I fought for was a lie.", 0)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/D/Male/3", 100)
sm.sayMonologue("Was the cruelty ever going to end?", 0)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/D/Male/4", 100)
sm.sayMonologue("Nothing I did seemed to make any difference.", 0)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/D/Male/5", 100)
sm.sayMonologue("\r\n\r\n\r\nI had committed unforgiveable acts in the name of peace...", 1)
sm.playExclSoundWithDownBGM("Voice4.img/Ark/Mono/D/Male/6", 100)
sm.blind(False, 0, 0, 0, 0, 1300)
sm.sendDelay(5000)
sm.showFadeTransition(0, 1000, 3000)
sm.zoomCamera(0, 1000, 2147483647, 2147483647, 2147483647)
sm.moveCamera(True, 0, 0, 0)
sm.sendDelay(300)
sm.removeOverlapScreen(1000)
sm.zoomCamera(0, 2000, 0, 600, 120)
sm.sendDelay(600)
sm.forcedMove(True, 30)
sm.sendDelay(1000)
sm.zoomCamera(1000, 2000, 1000, 800, 120)
sm.flipNpcByTemplateId(3001510, True)
sm.flipNpcByTemplateId(3001510, False)
sm.moveNpcByTemplateId(3001510, True, 30, 200)
sm.sendDelay(600)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(3001510) # Ferret
sm.sendNext("#face0#Ark, you're still not well. Do you need a break?")
sm.setInnerOverrideSpeakerTemplateID(3001500) # Ark
sm.sendSay("#face1#No, I'll keep up.")
sm.zoomCamera(1000, 2000, 1000, 900, 120)
sm.forcedMove(False, 130)
sm.sendDelay(1000)
sm.showFadeTransition(0, 1000, 3000)
sm.zoomCamera(0, 1000, 2147483647, 2147483647, 2147483647)
sm.moveCamera(True, 0, 0, 0)
sm.sendDelay(300)
sm.removeOverlapScreen(1000)
sm.moveCamera(True, 0, 0, 0)
sm.lockInGameUI(False, True)
sm.warp(402000648)