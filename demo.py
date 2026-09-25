DEMO_SIGNS={
 'পানি':{'en':'Water','context':'Need / request','confidence':94},
 'খাবার':{'en':'Food','context':'Need / request','confidence':92},
 'সাহায্য':{'en':'Help','context':'Assistance','confidence':96},
 'হাসপাতাল':{'en':'Hospital','context':'Healthcare','confidence':90},
 'ধন্যবাদ':{'en':'Thank you','context':'Courtesy','confidence':95},
 'আবার বলুন':{'en':'Please repeat','context':'Clarification','confidence':93},
}
def translate_demo(label):
 phrases={'পানি':'আমি পানি চাই।','খাবার':'আমার খাবার দরকার।','সাহায্য':'আমার সাহায্য দরকার।','হাসপাতাল':'আমাকে হাসপাতালে নিতে হবে।','ধন্যবাদ':'ধন্যবাদ।','আবার বলুন':'দয়া করে আবার বলুন।'}
 x=DEMO_SIGNS[label]; return {'bn':phrases[label],'en':x['en'],'confidence':x['confidence'],'context':x['context']}
