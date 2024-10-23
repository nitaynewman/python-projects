import unicodedata

emojis = ['😀', '😃', '😄', '😁','😆','😅','😂','🤣','🥲','🥹','☺️','😊','😇','🙂','🙃','😉','😌','😍','🥰','😘','😗','😙','😚','😋','😛','😝','😜','🤪','🤨','🧐','🤓','😎','🥸','🤩','🥳','🙂‍↕️','😏','😒','🙂‍↔️','😞','😔','😟','😕','🙁','☹️','😣','😖','😫','😩','🥺','😢','😭','😮‍💨','😤','😠','😡','🤬','🤯','😳','🥵','🥶','😱','😨','😰','😥','😓','🫣','🤗','🫡','🤔','🫢','🤭','🤫','🤥','😶','😶‍🌫️','😐','😑','😬','🫨','🫠','🙄','😯','😦','😧','😮','😲','🥱','😴','🤤','😪','😵','😵‍💫','🫥','🤐','🥴','🤢','🤮','🤧','😷','🤒','🤕','🤑','🤠','😈','👿','👹','👺','🤡','💩','👻','💀','☠️','👽','👾','🤖','🎃','😺','😸','😹','😻','😼','😽','🙀','😿','😾','👋','🤚','🖐','✋','🖖','👌','🤌','🤏','✌️','🤞','🫰','🤟','🤘','🤙','🫵','🫱','🫲','🫸','🫷','🫳','🫴','👈','👉','👆','🖕','👇','☝️','👍','👎','✊','👊','🤛','🤜','👏','🫶','🙌','👐','🤲','🤝','🙏','✍️','💅','🤳','💪','🦾','🦵','🦿','🦶','👣','👂','🦻','👃','🫀','🫁','🧠','🦷','🦴','👀','👁','👅','👄','🫦','💋','🩸','👶','👧','🧒','👦','👩','🧑','👨','👩‍🦱','🧑‍🦱','👨‍🦱','👩‍🦰','🧑‍🦰','👨‍🦰','👱‍♀️','👱','👱‍♂️','👩‍🦳','🧑‍🦳','👨‍🦳','👩‍🦲','🧑‍🦲','👨‍🦲','🧔‍♀️','🧔','🧔‍♂️','👵','🧓','👴','👲','👳‍♀️','👳','👳‍♂️','🧕','👮‍♀️','👮','👮‍♂️','👷‍♀️','👷','👷‍♂️','💂‍♀️','💂','💂‍♂️','🕵️‍♀️','🕵️','🕵️‍♂️','👩‍⚕️','🧑‍⚕️','👨‍⚕️','👩‍🌾','🧑‍🌾','👨‍🌾','👩‍🍳','🧑‍🍳','👨‍🍳','👩‍🎓','🧑‍🎓','👨‍🎓','👩‍🎤','🧑‍🎤','👨‍🎤','👩‍🏫','🧑‍🏫','👨‍🏫','👩‍🏭','🧑‍🏭','👨‍🏭','👩‍💻','🧑‍💻','👨‍💻','👩‍💼','🧑‍💼','👨‍💼','👩‍🔧','🧑‍🔧','👨‍🔧','👩‍🔬','🧑‍🔬','👨‍🔬','👩‍🎨','🧑‍🎨','👨‍🎨','👩‍🚒','🧑‍🚒','👨‍🚒','👩‍✈️','🧑‍✈️','👨‍✈️','👩‍🚀','🧑‍🚀','👨‍🚀','👩‍⚖️','🧑‍⚖️','👨‍⚖️','👰‍♀️','👰','👰‍♂️','🤵‍♀️','🤵','🤵‍♂️','👸','🫅','🤴','🥷','🦸‍♀️','🦸','🦸‍♂️','🦹‍♀️','🦹','🦹‍♂️','🤶','🧑‍🎄','🎅','🧙‍♀️','🧙','🧙‍♂️','🧝‍♀️','🧝','🧝‍♂️','🧛‍♀️','🧛','🧛‍♂️','🧟‍♀️','🧟','🧟‍♂️','🧞‍♀️','🧞','🧞‍♂️','🧜‍♀️','🧜','🧜‍♂️','🧚‍♀️','🧚','🧚‍♂️','🧌','👼','🤰','🫄','🫃','🤱','👩‍🍼','🧑‍🍼','👨‍🍼','🙇‍♀️','🙇','🙇‍♂️','💁‍♀️','💁','💁‍♂️','🙅‍♀️','🙅','🙅‍♂️','🙆‍♀️','🙆','🙆‍♂️','🙋‍♀️','🙋','🙋‍♂️','🧏‍♀️','🧏','🧏‍♂️','🤦‍♀️','🤦','🤦‍♂️','🤷‍♀️','🤷','🤷‍♂️','🙎‍♀️','🙎','🙎‍♂️','🙍‍♀️','🙍','🙍‍♂️','💇‍♀️','💇','💇‍♂️','💆‍♀️','💆','💆‍♂️','🧖‍♀️','🧖','🧖‍♂️','💅','🤳','💃','🕺','👯‍♀️','👯','👯‍♂️','🕴','👩‍🦽','👩‍🦽‍➡️','🧑‍🦽','🧑‍🦽‍➡️','👨‍🦽','👨‍🦽‍➡️','👩‍🦼','👩‍🦼‍➡️','🧑‍🦼','🧑‍🦼‍➡️','👨‍🦼','👨‍🦼‍➡️','🚶‍♀️','🚶‍♀️‍➡️','🚶','🚶‍➡️','🚶‍♂️','🚶‍♂️‍➡️','👩‍🦯','👩‍🦯‍➡️','🧑‍🦯','🧑‍🦯‍➡️','👨‍🦯','👨‍🦯‍➡️','🧎‍♀️','🧎‍♀️‍➡️','🧎','🧎‍➡️','🧎‍♂️','🧎‍♂️‍➡️','🏃‍♀️','🏃‍♀️‍➡️','🏃','🏃‍➡️','🏃‍♂️','🏃‍♂️‍➡️','🧍‍♀️','🧍','🧍‍♂️','👭','🧑‍🤝‍🧑','👬','👫','👩‍❤️‍👩','💑','👨‍❤️‍👨','👩‍❤️‍👨','👩‍❤️‍💋‍👩','💏','👨‍❤️‍💋‍👨','👩‍❤️‍💋‍👨','👪','👨‍👩‍👦','👨‍👩‍👧','👨‍👩‍👧‍👦','👨‍👩‍👦‍👦','👨‍👩‍👧‍👧','👨‍👨‍👦','👨‍👨‍👧','👨‍👨‍👧‍👦','👨‍👨‍👦‍👦','👨‍👨‍👧‍👧','👩‍👩‍👦','👩‍👩‍👧','👩‍👩‍👧‍👦','👩‍👩‍👦‍👦','👩‍👩‍👧‍👧','👨‍👦','👨‍👦‍👦','👨‍👧','👨‍👧‍👦','👨‍👧‍👧','👩‍👦','👩‍👦‍👦','👩‍👧','👩‍👧‍👦','👩‍👧‍👧','🧑‍🧑‍🧒','🧑‍🧑‍🧒‍🧒','🧑‍🧒','🧑‍🧒‍🧒','🗣','👤','👥','🫂','🧳','🌂','☂️','🧵','🪡','🪢','🪭','🧶','👓','🕶','🥽','🥼','🦺','👔','👕','👖','🧣','🧤','🧥','🧦','👗','👘','🥻','🩴','🩱','🩲','🩳','👙','👚','👛','👜','👝','🎒','👞','👟','🥾','🥿','👠','👡','🩰','👢','👑','👒','🎩','🎓','🧢','⛑','🪖','💄','💍','💼','👋🏻','🤚🏻','🖐🏻','✋🏻','🖖🏻','👌🏻','🤌🏻','🤏🏻','✌🏻','🤞🏻','🫰🏻','🤟🏻','🤘🏻','🤙🏻','🫵🏻','🫱🏻','🫲🏻','🫸🏻','🫷🏻','🫳🏻','🫴🏻','👈🏻','👉🏻','👆🏻','🖕🏻','👇🏻','☝🏻','👍🏻','👎🏻','✊🏻','👊🏻','🤛🏻','🤜🏻','👏🏻','🫶🏻','🙌🏻','👐🏻','🤲🏻','🙏🏻','✍🏻','💅🏻','🤳🏻','💪🏻','🦵🏻','🦶🏻','👂🏻','🦻🏻','👃🏻','👶🏻','👧🏻','🧒🏻','👦🏻','👩🏻','🧑🏻','👨🏻','👩🏻‍🦱','🧑🏻‍🦱','👨🏻‍🦱','👩🏻‍🦰','🧑🏻‍🦰','👨🏻‍🦰','👱🏻‍♀️','👱🏻','👱🏻‍♂️','👩🏻‍🦳','🧑🏻‍🦳','👨🏻‍🦳','👩🏻‍🦲','🧑🏻‍🦲','👨🏻‍🦲','🧔🏻‍♀️','🧔🏻','🧔🏻‍♂️','👵🏻','🧓🏻','👴🏻','👲🏻','👳🏻‍♀️','👳🏻','👳🏻‍♂️','🧕🏻','👮🏻‍♀️','👮🏻','👮🏻‍♂️','👷🏻‍♀️','👷🏻','👷🏻‍♂️','💂🏻‍♀️','💂🏻','💂🏻‍♂️','🕵🏻‍♀️','🕵🏻','🕵🏻‍♂️','👩🏻‍⚕️','🧑🏻‍⚕️','👨🏻‍⚕️','👩🏻‍🌾','🧑🏻‍🌾','👨🏻‍🌾','👩🏻‍🍳','🧑🏻‍🍳','👨🏻‍🍳','👩🏻‍🎓','🧑🏻‍🎓','👨🏻‍🎓','👩🏻‍🎤','🧑🏻‍🎤','👨🏻‍🎤','👩🏻‍🏫','🧑🏻‍🏫','👨🏻‍🏫','👩🏻‍🏭','🧑🏻‍🏭','👨🏻‍🏭','👩🏻‍💻','🧑🏻‍💻','👨🏻‍💻','👩🏻‍💼','🧑🏻‍💼','👨🏻‍💼','👩🏻‍🔧','🧑🏻‍🔧','👨🏻‍🔧','👩🏻‍🔬','🧑🏻‍🔬','👨🏻‍🔬','👩🏻‍🎨','🧑🏻‍🎨','👨🏻‍🎨','👩🏻‍🚒','🧑🏻‍🚒','👨🏻‍🚒','👩🏻‍✈️','🧑🏻‍✈️','👨🏻‍✈️','👩🏻‍🚀','🧑🏻‍🚀','👨🏻‍🚀','👩🏻‍⚖️','🧑🏻‍⚖️','👨🏻‍⚖️','👰🏻‍♀️','👰🏻','👰🏻‍♂️','🤵🏻‍♀️','🤵🏻','🤵🏻‍♂️','👸🏻','🫅🏻','🤴🏻','🥷🏻','🦸🏻‍♀️','🦸🏻','🦸🏻‍♂️','🦹🏻‍♀️','🦹🏻','🦹🏻‍♂️','🤶🏻','🧑🏻‍🎄','🎅🏻','🧙🏻‍♀️','🧙🏻','🧙🏻‍♂️','🧝🏻‍♀️','🧝🏻','🧝🏻‍♂️','🧛🏻‍♀️','🧛🏻','🧛🏻‍♂️','🧜🏻‍♀️','🧜🏻','🧜🏻‍♂️','🧚🏻‍♀️','🧚🏻','🧚🏻‍♂️','👼🏻','🤰🏻','🫄🏻','🫃🏻','🤱🏻','👩🏻‍🍼','🧑🏻‍🍼','👨🏻‍🍼','🙇🏻‍♀️','🙇🏻','🙇🏻‍♂️','💁🏻‍♀️','💁🏻','💁🏻‍♂️','🙅🏻‍♀️','🙅🏻','🙅🏻‍♂️','🙆🏻‍♀️','🙆🏻','🙆🏻‍♂️','🙋🏻‍♀️','🙋🏻','🙋🏻‍♂️','🧏🏻‍♀️','🧏🏻','🧏🏻‍♂️','🤦🏻‍♀️','🤦🏻','🤦🏻‍♂️','🤷🏻‍♀️','🤷🏻','🤷🏻‍♂️','🙎🏻‍♀️','🙎🏻','🙎🏻‍♂️','🙍🏻‍♀️','🙍🏻','🙍🏻‍♂️','💇🏻‍♀️','💇🏻','💇🏻‍♂️','💆🏻‍♀️','💆🏻','💆🏻‍♂️','🧖🏻‍♀️','🧖🏻','🧖🏻‍♂️','💃🏻','🕺🏻','🕴🏻','👩🏻‍🦽','👩🏻‍🦽‍➡️','🧑🏻‍🦽','🧑🏻‍🦽‍➡️','👨🏻‍🦽','👨🏻‍🦽‍➡️','👩🏻‍🦼','👩🏻‍🦼‍➡️','🧑🏻‍🦼','🧑🏻‍🦼‍➡️','👨🏻‍🦼','👨🏻‍🦼‍➡️','🚶🏻‍♀️','🚶🏻‍♀️‍➡️','🚶🏻','🚶🏻‍➡️','🚶🏻‍♂️','🚶🏻‍♂️‍➡️','👩🏻‍🦯','👩🏻‍🦯‍➡️','🧑🏻‍🦯','🧑🏻‍🦯‍➡️','👨🏻‍🦯','👨🏻‍🦯‍➡️','🧎🏻‍♀️','🧎🏻‍♀️‍➡️','🧎🏻','🧎🏻‍➡️','🧎🏻‍♂️','🧎🏻‍♂️‍➡️','🏃🏻‍♀️','🏃🏻‍♀️‍➡️','🏃🏻','🏃🏻‍➡️','🏃🏻‍♂️','🏃🏻‍♂️‍➡️','🧍🏻‍♀️','🧍🏻','🧍🏻‍♂️','👭🏻','🧑🏻‍🤝‍🧑🏻','👬🏻','👫🏻','🧗🏻‍♀️','🧗🏻','🧗🏻‍♂️','🏇🏻','🏂🏻','🏌🏻‍♀️','🏌🏻','🏌🏻‍♂️','🏄🏻‍♀️','🏄🏻','🏄🏻‍♂️','🚣🏻‍♀️','🚣🏻','🚣🏻‍♂️','🏊🏻‍♀️','🏊🏻','🏊🏻‍♂️','⛹🏻‍♀️','⛹🏻','⛹🏻‍♂️','🏋🏻‍♀️','🏋🏻','🏋🏻‍♂️','🚴🏻‍♀️','🚴🏻','🚴🏻‍♂️','🚵🏻‍♀️','🚵🏻','🚵🏻‍♂️','🤸🏻‍♀️','🤸🏻','🤸🏻‍♂️','🤽🏻‍♀️','🤽🏻','🤽🏻‍♂️','🤾🏻‍♀️','🤾🏻','🤾🏻‍♂️','🤹🏻‍♀️','🤹🏻','🤹🏻‍♂️','🧘🏻‍♀️','🧘🏻','🧘🏻‍♂️','🛀🏻','🛌🏻','👋🏼','🤚🏼','🖐🏼','✋🏼','🖖🏼','👌🏼','🤌🏼','🤏🏼','✌🏼','🤞🏼','🫰🏼','🤟🏼','🤘🏼','🤙🏼','🫵🏼','🫱🏼','🫲🏼','🫸🏼','🫷🏼','🫳🏼','🫴🏼','👈🏼','👉🏼','👆🏼','🖕🏼','👇🏼','☝🏼','👍🏼','👎🏼','✊🏼','👊🏼','🤛🏼','🤜🏼','👏🏼','🫶🏼','🙌🏼','👐🏼','🤲🏼','🙏🏼','✍🏼','💅🏼','🤳🏼','💪🏼','🦵🏼','🦶🏼','👂🏼','🦻🏼','👃🏼','👶🏼','👧🏼','🧒🏼','👦🏼','👩🏼','🧑🏼','👨🏼','👩🏼‍🦱','🧑🏼‍🦱','👨🏼‍🦱','👩🏼‍🦰','🧑🏼‍🦰','👨🏼‍🦰','👱🏼‍♀️','👱🏼','👱🏼‍♂️','👩🏼‍🦳','🧑🏼‍🦳','👨🏼‍🦳','👩🏼‍🦲','🧑🏼‍🦲','👨🏼‍🦲','🧔🏼‍♀️','🧔🏼','🧔🏼‍♂️','👵🏼','🧓🏼','👴🏼','👲🏼','👳🏼‍♀️','👳🏼','👳🏼‍♂️','🧕🏼','👮🏼‍♀️','👮🏼','👮🏼‍♂️','👷🏼‍♀️','👷🏼','👷🏼‍♂️','💂🏼‍♀️','💂🏼','💂🏼‍♂️','🕵🏼‍♀️','🕵🏼','🕵🏼‍♂️','👩🏼‍⚕️','🧑🏼‍⚕️','👨🏼‍⚕️','👩🏼‍🌾','🧑🏼‍🌾','👨🏼‍🌾','👩🏼‍🍳','🧑🏼‍🍳','👨🏼‍🍳','👩🏼‍🎓','🧑🏼‍🎓','👨🏼‍🎓','👩🏼‍🎤','🧑🏼‍🎤','👨🏼‍🎤','👩🏼‍🏫','🧑🏼‍🏫','👨🏼‍🏫','👩🏼‍🏭','🧑🏼‍🏭','👨🏼‍🏭','👩🏼‍💻','🧑🏼‍💻','👨🏼‍💻','👩🏼‍💼','🧑🏼‍💼','👨🏼‍💼','👩🏼‍🔧','🧑🏼‍🔧','👨🏼‍🔧','👩🏼‍🔬','🧑🏼‍🔬','👨🏼‍🔬','👩🏼‍🎨','🧑🏼‍🎨','👨🏼‍🎨','👩🏼‍🚒','🧑🏼‍🚒','👨🏼‍🚒','👩🏼‍✈️','🧑🏼‍✈️','👨🏼‍✈️','👩🏼‍🚀','🧑🏼‍🚀','👨🏼‍🚀','👩🏼‍⚖️','🧑🏼‍⚖️','👨🏼‍⚖️','👰🏼‍♀️','👰🏼','👰🏼‍♂️','🤵🏼‍♀️','🤵🏼','🤵🏼‍♂️','👸🏼','🫅🏼','🤴🏼','🥷🏼','🦸🏼‍♀️','🦸🏼','🦸🏼‍♂️','🦹🏼‍♀️','🦹🏼','🦹🏼‍♂️','🤶🏼','🧑🏼‍🎄','🎅🏼','🧙🏼‍♀️','🧙🏼','🧙🏼‍♂️','🧝🏼‍♀️','🧝🏼','🧝🏼‍♂️','🧛🏼‍♀️','🧛🏼','🧛🏼‍♂️','🧜🏼‍♀️','🧜🏼','🧜🏼‍♂️','🧚🏼‍♀️','🧚🏼','🧚🏼‍♂️','👼🏼','🤰🏼','🫄🏼','🫃🏼','🤱🏼','👩🏼‍🍼','🧑🏼‍🍼','👨🏼‍🍼','🙇🏼‍♀️','🙇🏼','🙇🏼‍♂️','💁🏼‍♀️','💁🏼','💁🏼‍♂️','🙅🏼‍♀️','🙅🏼','🙅🏼‍♂️','🙆🏼‍♀️','🙆🏼','🙆🏼‍♂️','🙋🏼‍♀️','🙋🏼','🙋🏼‍♂️','🧏🏼‍♀️','🧏🏼','🧏🏼‍♂️','🤦🏼‍♀️','🤦🏼','🤦🏼‍♂️','🤷🏼‍♀️','🤷🏼','🤷🏼‍♂️','🙎🏼‍♀️','🙎🏼','🙎🏼‍♂️','🙍🏼‍♀️','🙍🏼','🙍🏼‍♂️','💇🏼‍♀️','💇🏼','💇🏼‍♂️','💆🏼‍♀️','💆🏼','💆🏼‍♂️','🧖🏼‍♀️','🧖🏼','🧖🏼‍♂️','💃🏼','🕺🏼','🕴🏼','👩🏼‍🦽','👩🏼‍🦽‍➡️','🧑🏼‍🦽','🧑🏼‍🦽‍➡️','👨🏼‍🦽','👨🏼‍🦽‍➡️','👩🏼‍🦼','👩🏼‍🦼‍➡️','🧑🏼‍🦼','🧑🏼‍🦼‍➡️','👨🏼‍🦼','👨🏼‍🦼‍➡️','🚶🏼‍♀️','🚶🏼‍♀️‍➡️','🚶🏼','🚶🏼‍➡️','🚶🏼‍♂️','🚶🏼‍♂️‍➡️','👩🏼‍🦯','👩🏼‍🦯‍➡️','🧑🏼‍🦯','🧑🏼‍🦯‍➡️','👨🏼‍🦯','👨🏼‍🦯‍➡️','🧎🏼‍♀️','🧎🏼‍♀️‍➡️','🧎🏼','🧎🏼‍➡️','🧎🏼‍♂️','🧎🏼‍♂️‍➡️','🏃🏼‍♀️','🏃🏼‍♀️‍➡️','🏃🏼','🏃🏼‍➡️','🏃🏼‍♂️','🏃🏼‍♂️‍➡️','🧍🏼‍♀️','🧍🏼','🧍🏼‍♂️','👭🏼','🧑🏼‍🤝‍🧑🏼','👬🏼','👫🏼','🧗🏼‍♀️','🧗🏼','🧗🏼‍♂️','🏇🏼','🏂🏼','🏌🏼‍♀️','🏌🏼','🏌🏼‍♂️','🏄🏼‍♀️','🏄🏼','🏄🏼‍♂️','🚣🏼‍♀️','🚣🏼','🚣🏼‍♂️','🏊🏼‍♀️','🏊🏼','🏊🏼‍♂️','⛹🏼‍♀️','⛹🏼','⛹🏼‍♂️','🏋🏼‍♀️','🏋🏼','🏋🏼‍♂️','🚴🏼‍♀️','🚴🏼','🚴🏼‍♂️','🚵🏼‍♀️','🚵🏼','🚵🏼‍♂️','🤸🏼‍♀️','🤸🏼','🤸🏼‍♂️','🤽🏼‍♀️','🤽🏼','🤽🏼‍♂️','🤾🏼‍♀️','🤾🏼','🤾🏼‍♂️','🤹🏼‍♀️','🤹🏼','🤹🏼‍♂️','🧘🏼‍♀️','🧘🏼','🧘🏼‍♂️','🛀🏼','🛌🏼','🐶','🐱','🐭','🐹','🐰','🦊','🐻','🐼','🐻‍❄️','🐨','🐯','🦁','🐮','🐷','🐽','🐸','🐵','🙈','🙉','🙊','🐒','🐔','🐧','🐦','🐦‍⬛','🐤','🐣','🐥','🦆','🦅','🦉','🦇','🐺','🐗','🐴','🦄','🐝','🪱','🐛','🦋','🐌','🐞','🐜','🪰','🪲','🪳','🦟','🦗','🕷','🕸','🦂','🐢','🐍','🦎','🦖','🦕','🐙','🦑','🦐','🦞','🦀','🪼','🪸','🐡','🐠','🐟','🐬','🐳','🐋','🦈','🐊','🐅','🐆','🦓','🫏','🦍','🦧','🦣','🐘','🦛','🦏','🐪','🐫','🦒','🦘','🦬','🐃','🐂','🐄','🐎','🐖','🐏','🐑','🦙','🐐','🦌','🫎','🐕','🐩','🦮','🐕‍🦺','🐈','🐈‍⬛','🪽','🪶','🐓','🦃','🦤','🦚','🦜','🦢','🪿','🦩','🕊','🐇','🦝','🦨','🦡','🦫','🦦','🦥','🐁','🐀','🐿','🦔','🐾','🐉','🐲','🐦‍🔥','🌵','🎄','🌲','🌳','🌴','🪹','🪺','🪵','🌱','🌿','☘️','🍀','🎍','🪴','🎋','🍃','🍂','🍁','🍄','🍄‍🟫','🐚','🪨','🌾','💐','🌷','🪷','🌹','🥀','🌺','🌸','🪻','🌼','🌻','🌞','🌝','🌛','🌜','🌚','🌕','🌖','🌗','🌘','🌑','🌒','🌓','🌔','🌙','🌎','🌍','🌏','🪐','💫','⭐️','🌟','✨','⚡️','☄️','💥','🔥','🌪','🌈','☀️','🌤','⛅️','🌥','☁️','🌦','🌧','⛈','🌩','🌨','❄️','☃️',
          '⛄️','🌬','💨','💧','💦','🫧','☔️','☂️','🌊','🍏','🍎','🍐','🍊','🍋','🍋‍🟩','🍌','🍉','🍇','🍓','🫐','🍈','🍒','🍑','🥭','🍍','🥥','🥝','🍅','🍆','🥑','🥦','🫛','🥬','🥒','🌶','🫑','🌽','🥕','🫒','🧄','🧅','🫚','🥔','🍠','🫘','🥐','🥯','🍞','🥖','🥨','🧀','🥚','🍳','🧈','🥞','🧇','🥓','🥩','🍗','🍖','🦴','🌭','🍔','🍟','🍕','🫓','🥪','🥙','🧆','🌮','🌯','🫔','🥗','🥘','🫕','🥫','🍝','🍜','🍲','🍛','🍣','🍱','🥟','🦪','🍤','🍙','🍚','🍘','🍥','🥠','🥮','🍢','🍡','🍧','🍨','🍦','🥧','🧁','🍰','🎂','🍮','🍭','🍬','🍫','🍿','🍩','🍪','🌰','🥜','🍯','🥛','🍼','🫖','☕️','🍵','🧃','🥤','🧋','🫙','🍶','🍺','🍻','🥂','🍷','🫗','🥃','🍸','🍹','🧉','🍾','🧊','🥄','🍴','🍽','🥣','🥡','🥢','🧂','⚽️','🏀','🏈','⚾️','🥎','🎾','🏐','🏉','🥏','🎱','🪀','🏓','🏸','🏒','🏑','🥍','🏏','🪃','🥅','⛳️','🪁','🏹','🎣','🤿','🥊','🥋','🎽','🛹','🛼','🛷','⛸','🥌','🎿','⛷','🏂','🪂','🏋️‍♀️','🏋️','🏋️‍♂️','🤼‍♀️','🤼','🤼‍♂️','🤸‍♀️','🤸','🤸‍♂️','⛹️‍♀️','⛹️','⛹️‍♂️','🤺','🤾‍♀️','🤾','🤾‍♂️','🏌️‍♀️','🏌️','🏌️‍♂️','🏇','🧘‍♀️','🧘','🧘‍♂️','🏄‍♀️','🏄','🏄‍♂️','🏊‍♀️','🏊','🏊‍♂️','🤽‍♀️','🤽','🤽‍♂️','🚣‍♀️','🚣','🚣‍♂️','🧗‍♀️','🧗','🧗‍♂️','🚵‍♀️','🚵','🚵‍♂️','🚴‍♀️','🚴','🚴‍♂️','🏆','🥇','🥈','🥉','🏅','🎖','🏵','🎗','🎫','🎟','🎪','🤹','🤹‍♂️','🤹‍♀️','🎭','🩰','🎨','🎬','🎤','🎧','🎼','🎹','🥁','🪘','🪇','🎷','🎺','🪗','🎸','🪕','🎻','🪈','🎲','♟','🎯','🎳','🎮','🎰','🧩','🚗','🚕','🚙','🚌','🚎','🏎','🚓','🚑','🚒','🚐','🛻','🚚','🚛','🚜','🦯','🦽','🦼','🛴','🚲','🛵','🏍','🛺','🚨','🚔','🚍','🚘','🚖','🛞','🚡','🚠','🚟','🚃','🚋','🚞','🚝','🚄','🚅','🚈','🚂','🚆','🚇','🚊','🚉','✈️','🛫','🛬','🛩','💺','🛰','🚀','🛸','🚁','🛶','⛵️','🚤','🛥','🛳','⛴','🚢','⚓️','🛟','🪝','⛽️','🚧','🚦','🚥','🚏','🗺','🗿','🗽','🗼','🏰','🏯','🏟','🎡','🎢','🛝','🎠','⛲️','⛱','🏖','🏝','🏜','🌋','⛰','🏔','🗻','🏕','⛺️','🛖','🏠','🏡','🏘','🏚','🏗','🏭','🏢','🏬','🏣','🏤','🏥','🏦','🏨','🏪','🏫','🏩','💒','🏛','⛪️','🕌','🕍','🛕','🕋','⛩','🛤','🛣','🗾','🎑','🏞','🌅','🌄','🌠','🎇','🎆','🌇','🌆','🏙','🌃','🌌','🌉','🌁','⌚️','📱','📲','💻','⌨️','🖥','🖨','🖱','🖲','🕹','🗜','💽','💾','💿','📀','📼','📷','📸','📹','🎥','📽','🎞','📞','☎️','📟','📠','📺','📻','🎙','🎚','🎛','🧭','⏱','⏲','⏰','🕰','⌛️','⏳','📡','🔋','🪫','🔌','💡','🔦','🕯','🪔','🧯','🛢','🛍️','💸','💵','💴','💶','💷','🪙','💰','💳','💎','⚖️','🪮','🪜','🧰','🪛','🔧','🔨','⚒','🛠','⛏','🪚','🔩','⚙️','🪤','🧱','⛓','⛓️‍💥','🧲','🔫','💣','🧨','🪓','🔪','🗡','⚔️','🛡','🚬','⚰️','🪦','⚱️','🏺','🔮','📿','🧿','🪬','💈','⚗️','🔭','🔬','🕳','🩹','🩺','🩻','🩼','💊','💉','🩸','🧬','🦠','🧫','🧪','🌡','🧹','🪠','🧺','🧻','🚽','🚰','🚿','🛁','🛀','🧼','🪥','🪒','🧽','🪣','🧴','🛎','🔑','🗝','🚪','🪑','🛋','🛏','🛌','🧸','🪆','🖼','🪞','🪟','🛍','🛒','🎁','🎈','🎏','🎀','🪄','🪅','🎊','🎉','🪩','🎎','🏮','🎐','🧧','✉️','📩','📨','📧','💌','📥','📤','📦','🏷','🪧','📪','📫','📬','📭','📮','📯','📜','📃','📄','📑','🧾','📊','📈','📉','🗒','🗓','📆','📅','🗑','🪪','📇','🗃','🗳','🗄','📋','📁','📂','🗂','🗞','📰','📓','📔','📒','📕','📗','📘','📙','📚','📖','🔖','🧷','🔗','📎','🖇','📐','📏','🧮','📌','📍','✂️','🖊','🖋','✒️','🖌','🖍','📝','✏️','🔍','🔎','🔏','🔐','🔒','🔓','❤️','🩷','🧡','💛','💚','💙','🩵','💜','🖤','🩶','🤍','🤎','❤️‍🔥','❤️‍🩹','💔','❣️','💕','💞','💓','💗','💖','💘','💝','💟','☮️','✝️','☪️','🪯','🕉','☸️','✡️','🔯','🕎','☯️','☦️','🛐','⛎','♈️','♉️','♊️','♋️','♌️','♍️','♎️','♏️','♐️','♑️','♒️','♓️','🆔','⚛️','🉑','☢️','☣️','📴','📳','🈶','🈚️','🈸','🈺','🈷️','✴️','🆚','💮','🉐','㊙️','㊗️','🈴','🈵','🈹','🈲','🅰️','🅱️','🆎','🆑','🅾️','🆘','❌','⭕️','🛑','⛔️','📛','🚫','💯','💢','♨️','🚷','🚯','🚳','🚱','🔞','📵','🚭','❗️','❕','❓','❔','‼️','⁉️','🔅','🔆','〽️','⚠️','🚸','🔱','⚜️','🔰','♻️','✅','🈯️','💹','❇️','✳️','❎','🌐','💠','Ⓜ️','🌀','💤','🏧','🚾','♿️','🅿️','🛗','🈳','🈂️','🛂','🛃','🛄','🛅','🚹','🚺','🚼','⚧','🚻','🚮','🎦','🛜','📶','🈁','🔣','ℹ️','🔤','🔡','🔠','🆖','🆗','🆙','🆒','🆕','🆓','0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟','🔢',#'️⃣',*'️⃣','⏏️','▶️','⏸','⏯','⏹','⏺','⏭','⏮','⏩','⏪','⏫','⏬','◀️','🔼','🔽','➡️','⬅️','⬆️','⬇️','↗️','↘️','↙️','↖️','↕️','↔️','↪️','↩️','⤴️','⤵️','🔀','🔁','🔂','🔄','🔃','🎵','🎶','➕','➖','➗','✖️','🟰','♾','💲','💱','™️','©️','®️','〰️','➰','➿','🔚','🔙','🔛','🔝','🔜','✔️','☑️','🔘','🔴','🟠','🟡','🟢','🔵','🟣','⚫️','⚪️','🟤','🔺','🔻','🔸','🔹','🔶','🔷','🔳','🔲','▪️','▫️','◾️','◽️','◼️','◻️','🟥','🟧','🟨','🟩','🟦','🟪','⬛️','⬜️','🟫','🔈','🔇','🔉','🔊','🔔','🔕','📣','📢','👁‍🗨','💬','💭','🗯','♠️','♣️','♥️','♦️','🃏','🎴','🀄️','🕐','🕑','🕒','🕓','🕔','🕕','🕖','🕗','🕘','🕙','🕚','🕛','🕜','🕝','🕞','🕟','🕠','🕡','🕢','🕣','🕤','🕥','🕦','🕧','✢','✣','✤','✥','✦','✧','★','☆','✯','✡︎','✩','✪','✫','✬','✭','✮','✶','✷','✵','✸','✹','→','⇒','⟹','⇨','⇾','➾','⇢','☛','☞','➔','➜','➙','➛','➝','➞','♠︎','♣︎','♥︎','♦︎','♤','♧','♡','♢','♚','♛','♜','♝','♞','♟','♔','♕','♖','♗','♘','♙','⚀','⚁','⚂','⚃','⚄','⚅','🂠','⚈','⚉','⚆','⚇','𓀀','𓀁','𓀂','𓀃','𓀄','𓀅','𓀆','𓀇','𓀈','𓀉','𓀊','𓀋','𓀌','𓀍','𓀎','𓀏','𓀐','𓀑','𓀒','𓀓','𓀔','𓀕','𓀖','𓀗','𓀘','𓀙','𓀚','𓀛','𓀜','𓀝','🏳️','🏴','🏁','🚩','🏳️‍🌈','🏳️‍⚧️','🏴‍☠️','🇦🇫','🇦🇽','🇦🇱','🇩🇿','🇦🇸','🇦🇩','🇦🇴','🇦🇮','🇦🇶','🇦🇬','🇦🇷','🇦🇲','🇦🇼','🇦🇺','🇦🇹','🇦🇿','🇧🇸','🇧🇭','🇧🇩','🇧🇧','🇧🇾','🇧🇪','🇧🇿','🇧🇯','🇧🇲','🇧🇹','🇧🇴','🇧🇦','🇧🇼','🇧🇷','🇮🇴','🇻🇬','🇧🇳','🇧🇬','🇧🇫','🇧🇮','🇰🇭','🇨🇲','🇨🇦','🇮🇨','🇨🇻','🇧🇶','🇰🇾','🇨🇫','🇹🇩','🇨🇱','🇨🇳','🇨🇽','🇨🇨','🇨🇴','🇰🇲','🇨🇬','🇨🇩','🇨🇰','🇨🇷','🇨🇮','🇭🇷','🇨🇺','🇨🇼','🇨🇾','🇨🇿','🇩🇰','🇩🇯','🇩🇲','🇩🇴','🇪🇨','🇪🇬','🇸🇻','🇬🇶','🇪🇷','🇪🇪','🇪🇹','🇪🇺','🇫🇰','🇫🇴','🇫🇯','🇫🇮','🇫🇷','🇬🇫','🇵🇫','🇹🇫','🇬🇦','🇬🇲','🇬🇪','🇩🇪','🇬🇭','🇬🇮','🇬🇷','🇬🇱','🇬🇩','🇬🇵','🇬🇺','🇬🇹','🇬🇬','🇬🇳','🇬🇼','🇬🇾','🇭🇹','🇭🇳','🇭🇰','🇭🇺','🇮🇸','🇮🇳','🇮🇩','🇮🇷','🇮🇶','🇮🇪','🇮🇲','🇮🇱','🇮🇹','🇯🇲','🇯🇵','🎌','🇯🇪','🇯🇴','🇰🇿','🇰🇪','🇰🇮','🇽🇰','🇰🇼','🇰🇬','🇱🇦','🇱🇻','🇱🇧','🇱🇸','🇱🇷','🇱🇾','🇱🇮','🇱🇹','🇱🇺','🇲🇴','🇲🇰','🇲🇬','🇲🇼','🇲🇾','🇲🇻','🇲🇱','🇲🇹','🇲🇭','🇲🇶','🇲🇷','🇲🇺','🇾🇹','🇲🇽','🇫🇲','🇲🇩','🇲🇨','🇲🇳','🇲🇪','🇲🇸','🇲🇦','🇲🇿','🇲🇲','🇳🇦','🇳🇷','🇳🇵','🇳🇱','🇳🇨','🇳🇿','🇳🇮','🇳🇪','🇳🇬','🇳🇺','🇳🇫','🇰🇵','🇲🇵','🇳🇴','🇴🇲','🇵🇰','🇵🇼','🇵🇸','🇵🇦','🇵🇬','🇵🇾','🇵🇪','🇵🇭','🇵🇳','🇵🇱','🇵🇹','🇵🇷','🇶🇦','🇷🇪','🇷🇴','🇷🇺','🇷🇼','🇼🇸','🇸🇲','🇸🇦','🇸🇳','🇷🇸','🇸🇨','🇸🇱','🇸🇬','🇸🇽','🇸🇰','🇸🇮','🇬🇸','🇸🇧','🇸🇴','🇿🇦','🇰🇷','🇸🇸','🇪🇸','🇱🇰','🇧🇱','🇸🇭','🇰🇳','🇱🇨','🇵🇲','🇻🇨','🇸🇩','🇸🇷','🇸🇿','🇸🇪','🇨🇭','🇸🇾','🇹🇼','🇹🇯','🇹🇿','🇹🇭','🇹🇱','🇹🇬','🇹🇰','🇹🇴','🇹🇹','🇹🇳','🇹🇷','🇹🇲','🇹🇨','🇹🇻','🇻🇮','🇺🇬','🇺🇦','🇦🇪','🇬🇧','🏴󠁧󠁢󠁥󠁮󠁧󠁿','🏴󠁧󠁢󠁳󠁣󠁴󠁿','🏴󠁧󠁢󠁷󠁬󠁳󠁿','🇺🇳','🇺🇸','🇺🇾','🇺🇿','🇻🇺','🇻🇦','🇻🇪','🇻🇳','🇼🇫','🇪🇭','🇾🇪','🇿🇲','🇿🇼','🙂‍↔️','🙂‍↕️','🚶‍➡️','🚶🏻‍➡️','🚶🏼‍➡️','🚶🏽‍➡️','🚶🏾‍➡️','🚶🏿‍➡️','🚶‍➡️','🚶🏻‍➡️','🚶🏼‍➡️','🚶🏽‍➡️','🚶🏾‍➡️','🚶🏿‍➡️','🚶‍♀️‍➡️','🚶🏻‍♀️‍➡️','🚶🏼‍♀️‍➡️','🚶🏽‍♀️‍➡️','🚶🏾‍♀️‍➡️','🚶🏿‍♀️‍➡️','🚶‍♂️‍➡️','🚶🏻‍♂️‍➡️','🚶🏼‍♂️‍➡️','🚶🏽‍♂️‍➡️','🚶🏾‍♂️‍➡️','🚶🏿‍♂️‍➡️','🧎‍➡️','🧎🏻‍➡️','🧎🏼‍➡️','🧎🏽‍➡️','🧎🏾‍➡️','🧎🏿‍➡️','🧎‍♀️‍➡️','🧎🏻‍♀️‍➡️','🧎🏼‍♀️‍➡️','🧎🏽‍♀️‍➡️','🧎🏾‍♀️‍➡️','🧎🏿‍♀️‍➡️','🧎‍♂️‍➡️','🧎🏻‍♂️‍➡️','🧎🏼‍♂️‍➡️','🧎🏽‍♂️‍➡️','🧎🏾‍♂️‍➡️','🧎🏿‍♂️‍➡️','🧑‍🦯‍➡️','🧑🏻‍🦯‍➡️','🧑🏼‍🦯‍➡️','🧑🏽‍🦯‍➡️','🧑🏾‍🦯‍➡️','🧑🏿‍🦯‍➡️','👨‍🦯‍➡️','👨🏻‍🦯‍➡️','👨🏼‍🦯‍➡️','👨🏽‍🦯‍➡️', '👨🏾‍🦯‍➡️','👨🏿‍🦯‍➡️','👩‍🦯‍➡️','👩🏻‍🦯‍➡️','👩🏼‍🦯‍➡️','👩🏽‍🦯‍➡️','👩🏾‍🦯‍➡️','👩🏿‍🦯‍➡️','🧑‍🦼‍➡️','🧑🏻‍🦼‍➡️','🧑🏼‍🦼‍➡️','🧑🏽‍🦼‍➡️','🧑🏾‍🦼‍➡️','🧑🏿‍🦼‍➡️','👨‍🦼‍➡️','👨🏻‍🦼‍➡️','👨🏼‍🦼‍➡️','👨🏽‍🦼‍➡️','👨🏾‍🦼‍➡️','👨🏿‍🦼‍➡️','👩‍🦼‍➡️','👩🏻‍🦼‍➡️','👩🏼‍🦼‍➡️','👩🏽‍🦼‍➡️','👩🏾‍🦼‍➡️','🧑‍🦽‍➡️','🧑🏻‍🦽‍➡️','🧑🏼‍🦽‍➡️','🧑🏽‍🦽‍➡️','🧑🏾‍🦽‍➡️','🧑🏿‍🦽‍➡️','👨‍🦽‍➡️','👨🏻‍🦽‍➡️','👨🏼‍🦽‍➡️','👨🏽‍🦽‍➡️','👨🏾‍🦽‍➡️','👨🏿‍🦽‍➡️','👩‍🦽‍➡️','👩🏻‍🦽‍➡️','👩🏼‍🦽‍➡️','👩🏽‍🦽‍➡️','👩🏾‍🦽‍➡️','👩🏿‍🦽‍➡️','🏃‍➡️','🏃🏻‍➡️','🏃🏼‍➡️','🏃🏽‍➡️','🏃🏾‍➡️','🏃🏿‍➡️','🏃‍♀️‍➡️','🏃🏻‍♀️‍➡️','🏃🏼‍♀️‍➡️','🏃🏽‍♀️‍➡️','🏃🏾‍♀️‍➡️','🏃🏿‍♀️‍➡️','🏃‍♂️‍➡️','🏃🏻‍♂️‍➡️','🏃🏼‍♂️‍➡️','🏃🏽‍♂️‍➡️','🏃🏾‍♂️‍➡️','🏃🏿‍♂️‍➡️','🧑‍🧑‍🧒','🧑‍🧑‍🧒‍🧒','🧑‍🧒','🧑‍🧒‍🧒','🐦‍🔥','🍋‍🟩','🍄‍🟫','⛓️‍💥','🫨','🩷','🩵','🩶','🫸','🫸🏻','🫸🏼','🫸🏽','🫸🏾','🫸🏿','🫷','🫷🏻','🫷🏼','🫷🏽','🫷🏾','🫷🏿','🫏','🫎','🪿','🐦‍⬛','🪽','🪼','🪻','🫛','🫚','🪭','🪮','🪈','🪇','🪯','🛜','🫠','🫢','🫣','🫡','🫥','🫤','🥹','🫱','🫱🏻','🫱🏼','🫱🏽','🫱🏾','🫱🏿','🫲','🫲🏻','🫲🏼','🫲🏽','🫲🏾','🫲🏿','🫳','🫳🏻','🫳🏼','🫳🏽','🫳🏾','🫳🏿','🫴','🫴🏻','🫴🏼','🫴🏽','🫴🏾','🫴🏿','🫰','🫰🏻','🫰🏼','🫰🏽','🫰🏾','🫰🏿','🫵','🫵🏻','🫵🏼','🫵🏽','🫵🏾','🫵🏿','🫶','🫶🏻','🫶🏼','🫶🏽','🫶🏾','🫶🏿','🤝🏻','🤝🏼','🤝🏽','🤝🏾','🤝🏿','🫱🏻‍🫲🏼','🫱🏻‍🫲🏽','🫱🏻‍🫲🏾','🫱🏻‍🫲🏿','🫱🏼‍🫲🏻','🫱🏼‍🫲🏽','🫱🏼‍🫲🏾','🫱🏼‍🫲🏿','🫱🏽‍🫲🏻','🫱🏽‍🫲🏼','🫱🏽‍🫲🏾','🫱🏽‍🫲🏿','🫱🏾‍🫲🏻','🫱🏾‍🫲🏼','🫱🏾‍🫲🏽','🫱🏾‍🫲🏿','🫱🏿‍🫲🏻','🫱🏿‍🫲🏼','🫱🏿‍🫲🏽','🫱🏿‍🫲🏾','🫦','🫅','🫅🏻','🫅🏼','🫅🏽','🫅🏾','🫅🏿','🫃','🫃🏻','🫃🏼','🫃🏽','🫃🏾','🫃🏿','🫄','🫄🏻','🫄🏼','🫄🏽','🫄🏾','🫄🏿','🧌','🪸','🪷','🪹','🪺','🫘','🫗','🫙','🛝','🛞','🛟','🪬','🪩','🪫','🩼','🩻','🫧','🪪','🟰','😮‍💨','😵‍💫','😶‍🌫️','❤️‍🔥','❤️‍🩹','🧔‍♀️','🧔🏻‍♀️','🧔🏼‍♀️','🧔🏽‍♀️','🧔🏾‍♀️','🧔🏿‍♀️','🧔‍♂️','🧔🏻‍♂️','🧔🏼‍♂️','🧔🏽‍♂️','🧔🏾‍♂️','🧔🏿‍♂️','💑🏻','💑🏼','💑🏽','💑🏾','💑🏿','💏🏻','💏🏼','💏🏽','💏🏾','💏🏿','👨🏻‍❤️‍👨🏻','👨🏻‍❤️‍👨🏼','👨🏻‍❤️‍👨🏽','👨🏻‍❤️‍👨🏾','👨🏻‍❤️‍👨🏿','👨🏼‍❤️‍👨🏻','👨🏼‍❤️‍👨🏼','👨🏼‍❤️‍👨🏽','👨🏼‍❤️‍👨🏾','👨🏼‍❤️‍👨🏿','👨🏽‍❤️‍👨🏻','👨🏽‍❤️‍👨🏼','👨🏽‍❤️‍👨🏽','👨🏽‍❤️‍👨🏾','👨🏽‍❤️‍👨🏿','👨🏾‍❤️‍👨🏻','👨🏾‍❤️‍👨🏼','👨🏾‍❤️‍👨🏽','👨🏾‍❤️‍👨🏾','👨🏾‍❤️‍👨🏿','👨🏿‍❤️‍👨🏻','👨🏿‍❤️‍👨🏼','👨🏿‍❤️‍👨🏽','👨🏿‍❤️‍👨🏾','👨🏿‍❤️‍👨🏿','👩🏻‍❤️‍👨🏻','👩🏻‍❤️‍👨🏼','👩🏻‍❤️‍👨🏽','👩🏻‍❤️‍👨🏾','👩🏻‍❤️‍👨🏿','👩🏻‍❤️‍👩🏻','👩🏻‍❤️‍👩🏼','👩🏻‍❤️‍👩🏽','👩🏻‍❤️‍👩🏾','👩🏻‍❤️‍👩🏿','👩🏼‍❤️‍👨🏻','👩🏼‍❤️‍👨🏼','👩🏼‍❤️‍👨🏽','👩🏼‍❤️‍👨🏾','👩🏼‍❤️‍👨🏿','👩🏼‍❤️‍👩🏻','👩🏼‍❤️‍👩🏼','👩🏼‍❤️‍👩🏽','👩🏼‍❤️‍👩🏾','👩🏼‍❤️‍👩🏿','👩🏽‍❤️‍👨🏻','👩🏽‍❤️‍👨🏼','👩🏽‍❤️‍👨🏽','👩🏽‍❤️‍👨🏾','👩🏽‍❤️‍👨🏿','👩🏽‍❤️‍👩🏻','👩🏽‍❤️‍👩🏼','👩🏽‍❤️‍👩🏽','👩🏽‍❤️‍👩🏾','👩🏽‍❤️‍👩🏿','👩🏾‍❤️‍👨🏻','👩🏾‍❤️‍👨🏼','👩🏾‍❤️‍👨🏽','👩🏾‍❤️‍👨🏾','👩🏾‍❤️‍👨🏿','👩🏾‍❤️‍👩🏻','👩🏾‍❤️‍👩🏼','👩🏾‍❤️‍👩🏽','👩🏾‍❤️‍👩🏾','👩🏾‍❤️‍👩🏿','👩🏿‍❤️‍👨🏻','👩🏿‍❤️‍👨🏼','👩🏿‍❤️‍👨🏽','👩🏿‍❤️‍👨🏾','👩🏿‍❤️‍👨🏿','👩🏿‍❤️‍👩🏻','👩🏿‍❤️‍👩🏼','👩🏿‍❤️‍👩🏽','👩🏿‍❤️‍👩🏾','👩🏿‍❤️‍👩🏿','🧑🏻‍❤️‍🧑🏼','🧑🏻‍❤️‍🧑🏽','🧑🏻‍❤️‍🧑🏾','🧑🏻‍❤️‍🧑🏿','🧑🏼‍❤️‍🧑🏻','🧑🏼‍❤️‍🧑🏽','🧑🏼‍❤️‍🧑🏾','🧑🏼‍❤️‍🧑🏿','🧑🏽‍❤️‍🧑🏻','🧑🏽‍❤️‍🧑🏼','🧑🏽‍❤️‍🧑🏾','🧑🏽‍❤️‍🧑🏿','🧑🏾‍❤️‍🧑🏻','🧑🏾‍❤️‍🧑🏼','🧑🏾‍❤️‍🧑🏽','🧑🏾‍❤️‍🧑🏿','🧑🏿‍❤️‍🧑🏻','🧑🏿‍❤️‍🧑🏼','🧑🏿‍❤️‍🧑🏽','🧑🏿‍❤️‍🧑🏾','👨🏻‍❤️‍💋‍👨🏻','👨🏻‍❤️‍💋‍👨🏼','👨🏻‍❤️‍💋‍👨🏽','👨🏻‍❤️‍💋‍👨🏾','👨🏻‍❤️‍💋‍👨🏿','👨🏼‍❤️‍💋‍👨🏻','👨🏼‍❤️‍💋‍👨🏼','👨🏼‍❤️‍💋‍👨🏽','👨🏼‍❤️‍💋‍👨🏾','👨🏼‍❤️‍💋‍👨🏿','👨🏽‍❤️‍💋‍👨🏻','👨🏽‍❤️‍💋‍👨🏼','👨🏽‍❤️‍💋‍👨🏽','👨🏽‍❤️‍💋‍👨🏾','👨🏽‍❤️‍💋‍👨🏿','👨🏾‍❤️‍💋‍👨🏻','👨🏾‍❤️‍💋‍👨🏼','👨🏾‍❤️‍💋‍👨🏽','👨🏾‍❤️‍💋‍👨🏾','👨🏾‍❤️‍💋‍👨🏿','👨🏿‍❤️‍💋‍👨🏻','👨🏿‍❤️‍💋‍👨🏼','👨🏿‍❤️‍💋‍👨🏽','👨🏿‍❤️‍💋‍👨🏾','👨🏿‍❤️‍💋‍👨🏿','👩🏻‍❤️‍💋‍👨🏻','👩🏻‍❤️‍💋‍👨🏼','👩🏻‍❤️‍💋‍👨🏽','👩🏻‍❤️‍💋‍👨🏾','👩🏻‍❤️‍💋‍👨🏿','👩🏻‍❤️‍💋‍👩🏻','👩🏻‍❤️‍💋‍👩🏼','👩🏻‍❤️‍💋‍👩🏽','👩🏻‍❤️‍💋‍👩🏾','👩🏻‍❤️‍💋‍👩🏿','👩🏼‍❤️‍💋‍👨🏻','👩🏼‍❤️‍💋‍👨🏼','👩🏼‍❤️‍💋‍👨🏽','👩🏼‍❤️‍💋‍👨🏾','👩🏼‍❤️‍💋‍👨🏿','👩🏼‍❤️‍💋‍👩🏻','👩🏼‍❤️‍💋‍👩🏼','👩🏼‍❤️‍💋‍👩🏽','👩🏼‍❤️‍💋‍👩🏾','👩🏼‍❤️‍💋‍👩🏿','👩🏽‍❤️‍💋‍👨🏻','👩🏽‍❤️‍💋‍👨🏼','👩🏽‍❤️‍💋‍👨🏽','👩🏽‍❤️‍💋‍👨🏾','👩🏽‍❤️‍💋‍👨🏿','👩🏽‍❤️‍💋‍👩🏻','👩🏽‍❤️‍💋‍👩🏼','👩🏽‍❤️‍💋‍👩🏽','👩🏽‍❤️‍💋‍👩🏾','👩🏽‍❤️‍💋‍👩🏿','👩🏾‍❤️‍💋‍👨🏻','👩🏾‍❤️‍💋‍👨🏼','👩🏾‍❤️‍💋‍👨🏽','👩🏾‍❤️‍💋‍👨🏾','👩🏾‍❤️‍💋‍👨🏿','👩🏾‍❤️‍💋‍👩🏻','👩🏾‍❤️‍💋‍👩🏼','👩🏾‍❤️‍💋‍👩🏽','👩🏾‍❤️‍💋‍👩🏾','👩🏾‍❤️‍💋‍👩🏿','👩🏿‍❤️‍💋‍👨🏻','👩🏿‍❤️‍💋‍👨🏼','👩🏿‍❤️‍💋‍👨🏽','👩🏿‍❤️‍💋‍👨🏾','👩🏿‍❤️‍💋‍👨🏿','👩🏿‍❤️‍💋‍👩🏻','👩🏿‍❤️‍💋‍👩🏼','👩🏿‍❤️‍💋‍👩🏽','👩🏿‍❤️‍💋‍👩🏾','👩🏿‍❤️‍💋‍👩🏿','🧑🏻‍❤️‍💋‍🧑🏼','🧑🏻‍❤️‍💋‍🧑🏽','🧑🏻‍❤️‍💋‍🧑🏾','🧑🏻‍❤️‍💋‍🧑🏿','🧑🏼‍❤️‍💋‍🧑🏻','🧑🏼‍❤️‍💋‍🧑🏽','🧑🏼‍❤️‍💋‍🧑🏾','🧑🏼‍❤️‍💋‍🧑🏿','🧑🏽‍❤️‍💋‍🧑🏻','🧑🏽‍❤️‍💋‍🧑🏼','🧑🏽‍❤️‍💋‍🧑🏾','🧑🏽‍❤️‍💋‍🧑🏿','🧑🏾‍❤️‍💋‍🧑🏻','🧑🏾‍❤️‍💋‍🧑🏼','🧑🏾‍❤️‍💋‍🧑🏽','🧑🏾‍❤️‍💋‍🧑🏿','🧑🏿‍❤️‍💋‍🧑🏻','🧑🏿‍❤️‍💋‍🧑🏼','🧑🏿‍❤️‍💋‍🧑🏽','🧑🏿‍❤️‍💋‍🧑🏾'
          ]


def is_bmp_compatible(emoji):
    return all(ord(char) <= 0xFFFF for char in emoji)

bmp_emojis = [emoji for emoji in emojis if is_bmp_compatible(emoji)]

# Write BMP-compatible emojis to a file
with open("whatsapp_sender/bmp_emojis.txt", "w", encoding="utf-8") as file:
    for emoji in bmp_emojis:
        file.write(f"{emoji} is BMP compatible\n")

print("BMP-compatible emojis have been written to bmp_emojis.txt")