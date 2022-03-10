---
notetype: feed
---
## Legacy Code
```js
// 1. move to the page of the list
const moveToList = () => { return new Promise((resolve, reject) => {
	top.frames[0].moveEduTrainOnlineList()
	setTimeout(()=>{resolve(true)}, 2e3)
}) }

// 2. open a session
const openSession = async () => {
	const tbody = top.frames[0].document.querySelector('table.bbs_list_table > tbody')
	console.log('tbody', tbody)
	const trs = tbody.getElementsByTagName('tr')
	console.log('trs', trs)
	window.player = null
	for(let i = 0; i < trs.length; i++) {
		if (trs[i].querySelector('#tmpLrnComptYn').value == 'N') {
			console.log(trs[i].querySelector('.sbtn'))
			const temp = trs[i].querySelector('.sbtn').onclick.toString().split(/[\(\)\,]/g)
			console.log('temp', temp)
			const crswrId = temp[3].replace(/\'/g, '')*1
			const contsId = temp[4].replace(/\'/g, '')*1
			top.frames[0].document.querySelector('#crswrId').value = crswrId
			top.frames[0].document.querySelector('#contsId').value = contsId
			var sFeatures ='top=0,left=0, status=yes, scrollbars=no,  scroll=auto, width=800px, height=600px, resizable=yes, menubar=no'
			var sUrl='https://edu.deti.or.kr/lcms/initStudyPlayer.go'
			console.log('sFeatures, sUrl', sFeatures, sUrl)
			window.player = await window.open('', 'studyContPlayer' + i, sFeatures)
			console.log('window.player', window.player)
			top.frames[0].hpgClassMainVO.action=sUrl
			top.frames[0].hpgClassMainVO.target='studyContPlayer' + i
			top.frames[0].hpgClassMainVO.submit()
			window.player.focus()
			break
		}
	}
	return window.player ? window.player : false
}

let completeSession = (player = window.player) => { return new Promise(async(resolve, reject) => {
	//const scos = await player.document.getElementsByClassName('sco')
	const scos = await getScos()
	console.log('1. scos', scos)
	let i = 0
	let outerLoop = setInterval(async() => {
		// 페이지가 미완료라면
		if (scos[i].querySelector('.lrnStatus').value == 'N') {
			const api = player.frames[0].getAPI()
			api.startTime -= parseInt(700*Math.random()+300)*1e3
			player.frames[0].CMIMODEL_SaveProgressRage(256, 256)
		}
		else {
			i++
			if ( i >= scos.length ) {
				await moveToList()
				resolve(true)
			}
			player.frames[0].CMIMODEL_NextSco()
		}
	}, 5000)
	
}) }

let getScos = (player = window.player) => { return new Promise((resolve, reject) => {
	let scos = []
	let loop = setInterval(()=>{
		scos = player.document.getElementsByClassName('sco')
		if (scos.length) {
			console.log('scos 길이:', scos.length)
			clearInterval(loop)
			resolve(scos)
		}
	}, 1000)
	//
}) }

const pause = async (sec = 1) => {
	setTimeout(()=> { return true }, sec * 1000)
}

let main = async() => {
	await moveToList()
	window.player = {}
	do {
		console.log('순환 시작')
		window.player = await openSession()
		console.log('player 호출', window.player)
		if (!window.player) {
			console.log('player 없어서 탈출', window.player)
			break
		}
		console.log('수업 듣기 전')
		await completeSession()
		window.player.close()
		await pause()
		console.log('수업 들은 후')
	}
	while (window.player)
}

main()

```

#Torvalz 