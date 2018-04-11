// JavaScript Document
function suckerfish_zzjs(type, tag, parentId) {
if (window.attachEvent) {
window.attachEvent("onload", function() {
var sfEls = (parentId==null)?document.getElementsByTagName(tag):document.getElementById(parentId).getElementsByTagName(tag);
type(sfEls);
});
}
}
hover = function(sfEls) {
for (var i=0; i<sfEls.length; i++) {
sfEls[i].onmouseover=function() {
this.className+=" hover";
}
sfEls[i].onmouseout=function() {
this.className=this.className.replace(new RegExp(" hover\\b"), "");
}
}
}
suckerfish_zzjs(hover, "ul");
suckerfish_zzjs(hover, "li");


 // var a=document.getElementsByTagName("a");
 //   for(var i = 0; i< a.length; i++)
 //    {
 //       a[i].title=a[i].innerHTML;
	   // a[i].target="_blank";
 //  }
/*  
 function geci(d){ 
  var gc=document.getElementById(d);
      gc.onclick=function(){
      //alert(this.innerHTML);
      window.clipboardData.setData("Text",this.innerHTML);
	  alert("复制成功");
  }
 }
 geci("txt");
 geci("lrc");
 
*/ 
 var keyvalue="请输入要搜索的歌词内容";
 var key=document.getElementById("kewords");
 	 key.onblur=function(){
		 if(this.value=="")
		 this.value=keyvalue;
		 }
     key.onfocus=function(){
		 if(this.value==keyvalue)
		 this.value="";
		 }
 var submi=document.getElementById("submit");
 	 submi.onmouseover=function(){
		this.className='onsub';
	 }
	 submi.onmouseout=function(){
	    this.className=null;
	 }

	 submi.onclick=function(){
		var kwd = key.value.replace(/\s+|\'|or|&/g," ");
			  kwd = kwd.replace(/^\s+|\s+$/g,""); 
			  key.value=kwd;
		if(kwd==""||kwd==keyvalue){alert("搜索关键字不能为空！");return false;}		
	 }
