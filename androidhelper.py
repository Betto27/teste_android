import androidhelper

#droid = androidhelper.Android()
message = android.dialogGetInput('TTS', 'What would you like to say?').result
android.ttsSpeak(message)

