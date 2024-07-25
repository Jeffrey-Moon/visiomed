package Controller;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import Inter.Command;
import Service.DeleteCommService;
import Service.DeleteHandiService;
import Service.DeleteQnaReplyService;
import Service.DeleteQnaService;
import Service.DeleteStoryService;
import Service.EditPwService;
import Service.IdCheckService;
import Service.JoinService;
import Service.LoginService;
import Service.LogoutService;
import Service.QnaBoardService;
import Service.RegHandiService;
import Service.RegMediboxService;
import Service.SelectHandiService;
import Service.SelectMediService;
import Service.SelectQnaReplyService;
import Service.SelectQnaService;
import Service.StoryBoardService;
import Service.StoryLikeService;
import Service.UpdateInfoService;
import Service.UpdateQnaService;
import Service.UpdateStoryService;
import Service.WriteCommService;
import Service.WriteQnaReplyService;

@WebServlet("*.do")
public class FrontController extends HttpServlet {
	
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

		System.out.println("[FrontController]");
		
		Command com = null;
		String nextpage = null;
		
		String uri = request.getRequestURI();
//		System.out.println("uri : " + uri);
		String path = request.getContextPath();
//		System.out.println("path : " + path);
		String command = uri.substring(path.length() + 1);
		System.out.println("command : " + command);
		
		// ȸ�� ���� ���
		if(command.equals("JoinServiceCon.do")) {
			com = new JoinService();
			nextpage = com.execute(request, response);	
			
		// ���̵� �ߺ� Ȯ�� ���
		} else if(command.equals("IdCheckServiceCon.do")) {
			com = new IdCheckService();
			nextpage = com.execute(request, response);
		
		// �α��� ���
		} else if(command.equals("LoginServiceCon.do")) {
			com = new LoginService();
			nextpage = com.execute(request, response);
		
		// �α׾ƿ� ���
		} else if(command.equals("LogoutServiceCon.do")) {
			com = new LogoutService();
			nextpage = com.execute(request, response);
		
		// ��й�ȣ ���� ���
		} else if(command.equals("EditPwServiceCon.do")) {
			com = new EditPwService();
			nextpage = com.execute(request, response);
		
		// ����� ���� ��� ���
		} else if(command.equals("RegHandiServiceCon.do")) {
			com = new RegHandiService();
			nextpage = com.execute(request, response);	
			
		// ����� ���� ���� ���
		} else if(command.equals("DeleteHandiServiceCon.do")) {
			com = new DeleteHandiService();
			nextpage = com.execute(request, response);	
			
		// �� ��� ���
		} else if(command.equals("RegMediboxServiceCon.do")) {
			com = new RegMediboxService();
			nextpage = com.execute(request, response);	
			
			// ����� ��ü ��ȸ ���
		}else if(command.equals("SelectMediServiceCon.do")) {
			com = new SelectMediService();
			nextpage = com.execute(request, response);	
							
		// ����� ��ü ��ȸ ���
		}else if(command.equals("SelectHandiServiceCon.do")) {
			com = new SelectHandiService();
			nextpage = com.execute(request, response);	
			
			
		// ���� ���� �� �ۼ� ���
		} else if(command.equals("StoryBoardServiceCon.do")) {
			com = new StoryBoardService();
			nextpage = com.execute(request, response);
		
		// ���� ���� �� ���� ���
		} else if(command.equals("UpdateStoryServiceCon.do")) {	
			com = new UpdateStoryService();
			nextpage = com.execute(request, response);
		
		// ���� ���� �� ���� ���
		} else if(command.equals("DeleteStorySeriveCon.do")) {
			com = new DeleteStoryService();
			nextpage = com.execute(request, response);
			
		// ��� �ۼ� ���
		} else if(command.equals("WriteCommServiceCon.do")) {
			com = new WriteCommService();
			nextpage = com.execute(request, response);
		
		// ��� ���� ���
		} else if(command.equals("DeleteCommServiceCon.do")) {
			com = new DeleteCommService();
			nextpage = com.execute(request, response);
			
		// ���ƿ� ������Ʈ ���
		} else if(command.equals("StoryLikeServiceCon.do")) {
			com = new StoryLikeService();
			nextpage = com.execute(request, response);
		
		// �����ϱ� �� �ۼ� ���
		} else if(command.equals("QnaBoardServiceCon.do")) {
			com = new QnaBoardService();
			nextpage = com.execute(request, response);
		
		// �����ϱ� �� ���� ���
		} else if(command.equals("UpdateQnaServiceCon.do")) {
			com = new UpdateQnaService();
			nextpage = com.execute(request, response);
		
		// �����ϱ� �� ���� ���
		} else if(command.equals("DeleteQnaServiceCon.do")) {
			com = new DeleteQnaService();
			nextpage = com.execute(request, response);
		
		// ���� �亯 �ۼ� ���
		} else if(command.equals("WriteQnaReplyServiceCon.do")) {
			com = new WriteQnaReplyService();
			nextpage = com.execute(request, response);
			
		// ���� �亯 ���� ���
		} else if(command.equals("DeleteQnaReplyServiceCon.do")) {
			com = new DeleteQnaReplyService();
			nextpage = com.execute(request, response);
		
		// �� ���Ǳ� ��ȸ ���
		} else if(command.equals("SelectQnaServiceCon.do")) {
			com = new SelectQnaService();
			nextpage = com.execute(request, response);
			
		// �� ���� �亯 ��ȸ ���
		} else if(command.equals("SelectQnaReplyServiceCon.do")) {
			com = new SelectQnaReplyService();
			nextpage = com.execute(request, response);
		
		// �� ���� ���� ���
		} else if(command.equals("UpdateInfoServiceCon.do")) {
			com = new UpdateInfoService();
			nextpage = com.execute(request, response);
		}
		
		
		
		
		
		

		
		// nextpage�� �̵�
		if(nextpage != null) {
			response.sendRedirect(nextpage);
		}
	
	} // service �޼ҵ� ����������
	

}
