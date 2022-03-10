---
notetype: feed
---
```js
	// 1. move to the page of the list
	const moveToList = () => { return new Promise((resolve, reject) => {
		top.frames[0].moveEduTrainOnlineList()
		setTimeout(()=>{resolve(true)}, 2e3)
	}) }

	// 2. open a session
	const openSession = async () => {
		const tbody = top.frames[0].document.querySelector('table.bbs_list_table > tbody')
		const trs = tbody.getElementsByTagName('tr')
		window.player = null
		for(let i = 0; i < trs.length; i++) {
			if (trs[i].querySelector('#tmpLrnComptYn').value == 'N') {
				console.log(trs[i].querySelector('.sbtn'))
				const temp = trs[i].querySelector('.sbtn').onclick.toString().split(/[\(\)\,]/g)
				const crswrId = temp[3].replace(/\'/g, '')*1
				const contsId = temp[4].replace(/\'/g, '')*1
				top.frames[0].document.querySelector('#crswrId').value = crswrId
				top.frames[0].document.querySelector('#contsId').value = contsId
				var sFeatures ='top=0,left=0, status=yes, scrollbars=no,  scroll=auto, width=800px, height=600px, resizable=yes, menubar=no'
				var sUrl='https://edu.deti.or.kr/lcms/initStudyPlayer.go'
				window.player = window.open('', 'studyContPlayer', sFeatures)
				top.frames[0].hpgClassMainVO.action=sUrl
				top.frames[0].hpgClassMainVO.target='studyContPlayer'
				top.frames[0].hpgClassMainVO.submit()
				window.player.focus
				break
			}
		}
		return window.player ? window.player : false
	}

	let completeSession = (player = window.player) => { return new Promise(async(resolve, reject) => {
		const scos = await getScos()
		console.log('1. scos', scos)
		let i = 0
		let outerLoop = setInterval(async() => {
			let a = await player.frames[0].getAPI()
			let isDone = await a.GetValue("cmi.progress_measure")*1
			if (isDone < 1) {
				const startTime = player.map.get("startTime") * 1 - parseInt(700*Math.random()+300)*1e3
				console.log(player.map.get("startTime"), startTime)
				if (player.map.get("startTime") && player.map.get("startTime")*1 > 0) await player.map.put("startTime", startTime)
				await a.SetValue("cmi.progress_measure", 1)
				await a.SetValue("cmi.completion_status", "complete")
				result = await player.ajaxCall({
					url : player.contextPath + '/lcms/scorm/ajax/Commit.go',
					async : false,
					type : 'POST',
					ajaxId : "",
					method : "",
					data : player.map,
					validationForm : ""
				});
			}
			else {
				i++
				if ( i >= scos.length ) {
					await moveToList()
					resolve(true)
				}
				player.launchItem(scos[i].id)
			}
		}, 5000)
	}) }

	let getScos = (player = window.player) => { return new Promise((resolve, reject) => {
		let scos = []
		let loop = setInterval(()=>{
			scos = player.document.getElementsByClassName('sco')
			if (scos.length) {
				clearInterval(loop)
				resolve(scos)
			}
		}, 1000)
	}) }

	let main = async() => {
		await moveToList()
		window.player = {}
		do {
			console.log('ìˆœí™˜ ì‹œìž‘')
			window.player = await openSession()
			console.log('player í˜¸ì¶œ', window.player)
			if (!window.player) {
				console.log('player ì—†ì–´ì„œ íƒˆì¶œ', window.player)
				break
			}
			console.log('ìˆ˜ì—… ë“£ê¸° ì „')
			await completeSession()
		}
		while (window.player)
	}

	main()
```
#Torvalz 