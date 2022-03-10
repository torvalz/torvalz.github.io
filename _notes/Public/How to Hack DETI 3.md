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
	//const scos = await player.document.getElementsByClassName('sco')
	const scos = await getScos()
	console.log('1. scos', scos)
	let i = 0
	let outerLoop = setInterval(async() => {
		// 페이지가 미완료라면
		//if (scos[i].querySelector('.lrnStatus').value == 'N') {
		let a = await top.frames[0]
		let isDone = await a.apiHandle.GetValue("cmi.progress_measure")*1
		if (isDone < 1) {
			// 시간 조작
			// 진도 완료
			console.log('시간 및 진도 조작 시작')
			await a.apiHandle.SetValue("cmi.progress_measure", 1)
			await a.apiHandle.SetValue("cmi.completion_status", "complete")
			result = await ajaxCall({
				url : contextPath + '/lcms/scorm/ajax/Commit.go',
				async : false,
				type : 'POST',
				ajaxId : "",
				method : "",
				data : map,
				validationForm : ""
			});
			console.log('시간 및 진도 조작 끝')
		}
		else {
			i++
			if ( i >= scos.length ) {
				await moveToList()
				resolve(true)
			}
			// 다음강
			player.launchItem(scos[i].id)
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
		console.log('수업 들은 후')
	}
	while (window.player)
}

main()
```
#Torvalz 
