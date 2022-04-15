let n = 1;

function gallery(num){

    //5 이상이되면 다시 1로, 1이하로 가면 5로
    
    n += num
    
    if (n<1){
        n=5
    }
    if (n>5){
        n=1
    }
    let imPath =  document.getElementById("photo"); //.getAttribute("src")
    imPath.setAttribute('src',"images/so"+(n)+".jpg")

    let viewN =  document.getElementById("viewNum");
    viewN.innerText=n;


    
}



// function loginBtn(){

//     let uid = prompt('아이디를 입력하세요')
//     let upw = prompt('비밀번호를 입력하세요')

//     login(uid,upw) // 로그인함수 호출,  매개변수 전달

// }
// let adminId = 'admin';
// let adminPw = '1111';

// function login(uid,upw){
//     if(uid == adminId && upw == adminPw){
//         alert('로그인 성공')
//         location.href='http://www.naver.com'
//     }
//     else{
//         alert('id 또는 pwd가 일치하지 않습니다.')
//     }
    

// }
// function sum1(){
//     let a =parseInt(prompt('숫자를 입력하세요','0'));
//     let b = parseInt(prompt('숫자를 입력하세요','0'));
//     let total = 0;
//     //a~b 까지의 합을 출력하는 프로그램 구성 
//     for (let i = a ; i<=b ; i++){
//         total += i;

//     }

//     document.write(total)


// }