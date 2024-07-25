<%@ page import="Model.UserDTO"%>
<%@ page language="java" contentType="text/html; charset=utf-8"
	pageEncoding="utf-8"%>
<!DOCTYPE html>
<html>
<head>
<title>VisioMed</title>
<meta charset="utf-8" />
<meta name="viewport"
	content="width=device-width, initial-scale=1, user-scalable=no" />
<link rel="stylesheet" href="assets/css/main.css" />
<link rel="stylesheet" href="assets/css/style.css" />

<style>
@font-face {
    font-family: 'Poppins', sans-serif;
    font-weight: normal;
    font-style: normal;
}
body {
    font-family: 'Poppins', sans-serif;
    background-image: url('images/bgimg_1.jpg');
    background-size: 100% 80%;
    padding-bottom: 100px;
    background-repeat: no-repeat;
}
</style>

</head>
<body class="landing is-preload" style="padding:0px">

	<%
		request.setCharacterEncoding("utf-8");

		String check = request.getParameter("check");
		String status = request.getParameter("status");

		String mo_title = "";
		String mo_content = "";

		UserDTO udto = (UserDTO)session.getAttribute("udto");
	%>

	<div id="page-wrapper">
		<!-- Header -->
		<header id="header" class="alt">
			<h1 style="color: black;font-size:xx-large;top:30px;">
				<a href="Index.jsp" style="color: black;font-size:55px;">VisioMed&nbsp;&nbsp;</a>
			</h1>
			
			<nav id="nav" style="text-align:right;">
				<i class="fa-regular fa-envelope fa-2x" style="color:black;margin-top:20px;"></i> 
				<i class="fa-solid fa-heart fa-2x" style="color:red;margin-left:20px;"></i> 
				<i class="fa-regular fa-pen-to-square fa-2x" style="color:black;margin-left:20px;"></i> 
				<i class="fa-solid fa-user fa-2x" style="color:gray;margin-left:20px;"></i>
				
				<% if (udto != null) { %>
					<sup style="color:green;font-weight:500;font-size:larger; vertical-align:sub;">
						&nbsp;&nbsp;<%= udto.getUser_name() %>님 로그인
					</sup>
				<% } %>
				
				<ul>
					<li><a href="Index.jsp" style="color:#696969;font-size:xx-large;">홈</a></li>
					<li><a href="select_handi.jsp" style="color:#696969;font-size:xx-large;">정보 등록 및 조회&nbsp;&nbsp;&nbsp;<i class='icon solid fa fa-angle-down'></i></a>
						<ul>
							<li><a href="reg_handi.jsp">회원 정보 등록</a></li>
						</ul>
					</li>
					<li class='sub-menu'><a href="#" style="color:#696969;font-size:xx-large;">커뮤니티&nbsp;&nbsp;&nbsp;<i class='fa fa-angle-down'></i></a>
						<ul>
							<li><a href="qnaMain.jsp">문의하기</a></li>
							<li><a href="storyMain.jsp">정보 공유</a></li>
						</ul>
					</li>
					<li class='sub-menu'><a href="Mypage.jsp" style="color:#696969;font-size:xx-large;">마이페이지</a></li>

					<% if (udto != null) { %>
						<li><a href="LogoutServiceCon.do" class="button" style="color: black;font-size:xx-large;">로그아웃</a></li>
					<% } else { %>
						<li><a href="Login.jsp" class="button" style="color:#816259;font-size:xx-large;">로그인</a></li>
					<% } %>
				</ul>
			</nav>
		</header>
		
		<!-- Banner -->
		<section id="banner">
			<!-- CTA -->	
			<section id="cta" style="height: 500px;">
				<% if (udto != null) { %>
					<h3 class="big-font" style="color:white;display:inline;">
						<%= udto.getUser_name() %>님, VisioMed 홈페이지에 들어온 것을 환영합니다!<br>
						제품 사용 방법을 알고 싶으면 아래 제품 설명 및 사용 방법 버튼을 눌러주세요.
					</h3>
					<br><br>
					<a href="Explain.jsp" class="button" style="color:#671909;border-radius:50px;font-size: xx-large;margin-top:70px">제품 설명 및 사용 방법</a>
				<% } else { %>
					<h2 style="color:white;">사용하기 쉬운 VisioMed로 안전하게 약을 복용하세요</h2>
					<p style="color:white;font-size:xx-large;">
						버튼만 누르면 먹을 약을 알려주고 섭취까지 확인하는<br>스마트한 약 보관함
					</p>
					<a href="Join.jsp" class="button" style="min-width:7em;border-radius:50px;font-size: xx-large;color: #671909;">회원가입</a>
					<a href="Explain.jsp" class="button" style="color:#671909;border-radius:50px;font-size: xx-large;">제품 설명 및 사용 방법</a>
				<% } %>
			</section>
		</section>

		<!-- Modal -->
		<div id="modal" class="modal-overlay">
			<%
				if (status == null) {
					// 상황별 모달 출력문
				} else if (check.equals("1") && status.equals("1")) {
					mo_title = "가입 성공";
					mo_content = "가입을 환영합니다";
				} else if (check.equals("1") && status.equals("2")) {
					mo_title = "가입 실패";
					mo_content = "양식을 다시 한번 확인해주세요";
				} else if (check.equals("1") && status.equals("3")) {
					mo_title = "3 성공";
					mo_content = "3 환영합니다";
				}
			%>

			<div class="modal-window">
				<div class="title">
					<h2><%= mo_title %></h2>
				</div>
				<div class="close-area">X</div>
				<div class="content">
					<p><%= mo_content %></p>
				</div>
			</div>
		</div>

		<!-- Modal Logic -->
		<script>
			const modal = document.getElementById("modal");
			function modalOn() {
			    modal.style.display = "flex";
			}
			function isModalOn() {
			    return modal.style.display === "flex";
			}
			function modalOff() {
			    modal.style.display = "none";
			}
			const closeBtn = modal.querySelector(".close-area");
			closeBtn.addEventListener("click", e => {
			    modalOff();
			});
			modal.addEventListener("click", e => {
			    const evTarget = e.target;
			    if (evTarget.classList.contains("modal-overlay")) {
			        modalOff();
			    }
			});
			window.addEventListener("keyup", e => {
			    if (isModalOn() && e.key === "Escape") {
			        modalOff();
			    }
			});
			window.onload = function () {
			    let qr_check = "1";
			    if (qr_check == <%= check %>) {
			        modalOn();
			    }
			};
		</script>

		<!-- Footer -->
		<footer id="footer" style="padding:3em 0 3em 0;">
			<div class="inner">
				<a href="#" class="page-top" style="position: relative;left:350px;">위로가기</a>
				<p style="margin:0 0 0 0;">전화: (+82)010-2512-5397</p>
				<p style="margin:0 0 0 0;">주소: 서울시, 성북구, 성북로 176</p>
				<span><img src="images/visiomed_logo.png" style="width:75px;"></span><br>
				<p class="copyright" style="margin:0 0 0 0;">copyrightⓒ 2024 All rights reserved by Team.VisioMed</p>
			</div>
		</footer>
	</div>

	<!-- Scripts -->
	<script src="assets/js/jquery.min.js"></script>
	<script src="assets/js/jquery.dropotron.min.js"></script>
	<script src="assets/js/jquery.scrollex.min.js"></script>
	<script src="assets/js/browser.min.js"></script>
	<script src="assets/js/breakpoints.min.js"></script>
	<script src="assets/js/util.js"></script>
	<script src="assets/js/main.js"></script>
	<script src="assets/js/bootstrap.js"></script>
	<script src="assets/js/bootstrap.min.js"></script>
	<script src="https://kit.fontawesome.com/8b21a455c5.js" crossorigin="anonymous"></script>

</body>
</html>
