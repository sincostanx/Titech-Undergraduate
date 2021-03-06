import com.jogamp.opengl.*;
import com.jogamp.opengl.util.PMVMatrix;
import com.jogamp.newt.event.MouseListener;
import com.jogamp.newt.event.MouseEvent;
import com.jogamp.newt.event.KeyListener;
import com.jogamp.newt.event.KeyEvent;

import java.lang.Math;

public class SimpleRotation implements GLEventListener{
  final Object3D obj;
  final PMVMatrix mats;
  final Shader shader;
  int uniformMat;
  int uniformLight;
  float t=0;
  static final int SCREENH=320;
  static final int SCREENW=320;

  public SimpleRotation(){
    obj = new Cube();
    mats = new PMVMatrix();
    shader = new Shader("resource/simple.vert", "resource/simple.frag");
  }

  public void init(GLAutoDrawable drawable){
    final GL2GL3 gl = drawable.getGL().getGL2GL3();
    if(gl.isGL4()){
      drawable.setGL(new DebugGL4(drawable.getGL().getGL4()));
    }else if(gl.isGL3()){
      drawable.setGL(new DebugGL3(drawable.getGL().getGL3()));
    }else if(gl.isGL2()){
      drawable.setGL(new DebugGL2(drawable.getGL().getGL2()));
    }
    //drawable.getGL().getGL2();
    gl.glViewport(0, 0, SCREENW, SCREENH);

    // Clear color buffer with black
    gl.glClearColor(1.0f, 0.5f, 1.0f, 1.0f);
    gl.glClearDepth(1.0f);
    gl.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT);
    gl.glEnable(GL2.GL_DEPTH_TEST);
    gl.glPixelStorei(GL.GL_UNPACK_ALIGNMENT,1);
    gl.glFrontFace(GL.GL_CCW);
    gl.glEnable(GL.GL_CULL_FACE);
    gl.glCullFace(GL.GL_BACK);

    gl.glCreateShader(GL2GL3.GL_VERTEX_SHADER);
    shader.init(gl);
    int programName =shader.getID();
    gl.glBindAttribLocation(programName,Object3D.VERTEXPOSITION, "inposition");
    gl.glBindAttribLocation(programName,Object3D.VERTEXCOLOR, "incolor");
    gl.glBindAttribLocation(programName,Object3D.VERTEXNORMAL, "innormal");
    gl.glBindAttribLocation(programName,Object3D.VERTEXTEXCOORD0,"intexcoord0");
    shader.link(gl);
    uniformMat = gl.glGetUniformLocation(programName, "mat");
    uniformLight = gl.glGetUniformLocation(programName, "lightdir");
    gl.glUseProgram(programName);
    gl.glUniform3f(uniformLight, 0f, 10f, -10f);
    obj.init(gl, mats, programName);
    gl.glUseProgram(0);
  }

  public void display(GLAutoDrawable drawable){
    final GL2GL3 gl = drawable.getGL().getGL2GL3();
    gl.glUseProgram(shader.getID());
    gl.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT);
    mats.glMatrixMode(GL2.GL_PROJECTION);
    mats.glLoadIdentity();
    mats.glFrustumf(-0.5f,0.5f,-0.5f,0.5f,1f,100f);

    mats.glMatrixMode(GL2.GL_MODELVIEW);
    mats.glLoadIdentity(); /* set 4x4 identity matrix, I*/
    mats.glTranslatef(0f,0f,-18.0f); /* multiply translation matrix, I*T */
    gl.glUniformMatrix4fv(uniformMat, 4, false, mats.glGetPMvMvitMatrixf());
    obj.display(gl, mats, shader.getID()); /* I*T*obj */
    
    t = t+0.3f;
    
    /* parameters for earth rotation around sun */
    float r = 6f;
    float scaling_ratio = 0.3f;
    float angle = (360f/365f)*t - 360f*(float)Math.floor((360f/365f)*t/360f);
    float rad = (float)Math.toRadians(angle);
    float x = -r*(float)Math.cos(rad);
    float y = -r*(float)Math.sin(rad);
    
    mats.glTranslatef(x, y, 0f);
    mats.glScalef(scaling_ratio, scaling_ratio, scaling_ratio);
    mats.update();
    gl.glUniformMatrix4fv(uniformMat, 4, false, mats.glGetPMvMvitMatrixf());
    obj.display(gl, mats, shader.getID());
    
    /* parameters for moon rotation around earth */
    r = 3f;
    scaling_ratio = 0.2f;
    angle = (360f/27.3f)*t - 360f*(float)Math.floor((360f/27.3f)*t/360f);
    rad = (float)Math.toRadians(angle);
    x = -r*(float)Math.cos(rad);
    y = -r*(float)Math.sin(rad);
    
    mats.glTranslatef(x, y, 0f);
    mats.glScalef(scaling_ratio, scaling_ratio, scaling_ratio);
    mats.update();
    gl.glUniformMatrix4fv(uniformMat, 4, false, mats.glGetPMvMvitMatrixf());
    obj.display(gl, mats, shader.getID());

    gl.glUseProgram(0);
  }

  public void reshape(GLAutoDrawable drawable, int x, int y, int w, int h){
  }

  public void dispose(GLAutoDrawable drawable){
  }

  public KeyListener createKeyListener(){
    return new simpleExampleKeyListener();
  }

  public MouseListener createMouseListener(){
    return new simpleExampleMouseListener();
  }
  
  public static void main(String[] args){
    SimpleRotation t = new SimpleRotation();
    new SimpleExampleBase("SimpleRotation", t, SCREENW, SCREENH).
      addKeyListener(t.createKeyListener()).
      addMouseListener(t.createMouseListener()).
      start();
  }

  class simpleExampleKeyListener implements KeyListener{
    public void keyPressed(KeyEvent e){
      int keycode = e.getKeyCode();
      System.out.print(keycode);
      if(java.awt.event.KeyEvent.VK_LEFT == keycode){
        System.out.print("a");
      }
    }
    public void keyReleased(KeyEvent e){
    }
    public void keyTyped(KeyEvent e){
    }
  }

  class simpleExampleMouseListener implements MouseListener{
    public void mouseDragged(MouseEvent e){
      System.out.println("dragged:"+e.getX()+" "+e.getY());
    }
    public void mouseMoved(MouseEvent e){
      System.out.println("moved:"+e.getX()+" "+e.getY());
    }
    public void mouseWheelMoved(MouseEvent e){
    }
    public void mouseClicked(MouseEvent e){
    }
    public void mouseEntered(MouseEvent e){
    }
    public void mouseExited(MouseEvent e){
    }
    public void mousePressed(MouseEvent e){
      System.out.println("pressed:"+e.getX()+" "+e.getY());
    }
    public void mouseReleased(MouseEvent e){
    }
  }
}
