//Cross-browser method to get an object
function getObject(id)
{
  if (document.getElementById)
    //IE 5.x or NS 6.x or above
    return document.getElementById(id);
  else if (document.all)
    //IE 4.x
    return document.all[id];
  else
    //Netscape 4.x
    return document[id];
}
// eof
