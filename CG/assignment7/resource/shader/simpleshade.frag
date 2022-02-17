//#version 120
//
// simple.frag
//
//uniform mat4 mat;
uniform sampler2D texture0;
uniform vec3 lightpos;
uniform vec3 lightcolor;
varying vec3 normal;
varying vec4 color;
varying vec2 texcoord;
varying vec3 position;

void main (void)
{
  float kd = dot(normalize(normal),normalize(lightpos-position));
  gl_FragColor = vec4(lightcolor*color.xyz*kd,1.0);
// gl_FragColor = 
//  gl_FragColor = vec4(0.3, 0.8, 0.2, 1.0);
//  vec2 dfdx = abs(dFdx(texcoord));
//  vec2 dfdy = abs(dFdy(texcoord));
//  float d = max(max(dfdx.x,dfdx.y),max(dfdy.x,dfdy.y));
//  gl_FragColor = vec4(d*20.0,0,0,1);
//gl_FragColor = vec4((0.9*max(dot(normal, normalize(lightdir)),0.0)+0.1)*color.xyz,1.0);
//  gl_FragColor = vec4(1.0,0.8,0.3,1.0);
}

