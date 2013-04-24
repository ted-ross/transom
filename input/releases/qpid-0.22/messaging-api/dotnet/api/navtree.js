var NAVTREE =
[
  [ "Qpid .NET Messaging API", "index.html", [
    [ "Class List", "annotated.html", [
      [ "Org::Apache::Qpid::Messaging::Address", "classOrg_1_1Apache_1_1Qpid_1_1Messaging_1_1Address.html", null ],
      [ "Org::Apache::Qpid::Messaging::SessionReceiver::CallbackServer", "classOrg_1_1Apache_1_1Qpid_1_1Messaging_1_1SessionReceiver_1_1CallbackServer.html", null ],
      [ "Org::Apache::Qpid::Messaging::Connection", "classOrg_1_1Apache_1_1Qpid_1_1Messaging_1_1Connection.html", null ],
      [ "Org::Apache::Qpid::Messaging::SessionReceiver::EventEngine", "classOrg_1_1Apache_1_1Qpid_1_1Messaging_1_1SessionReceiver_1_1EventEngine.html", null ],
      [ "Org::Apache::Qpid::Messaging::FailoverUpdates", "classOrg_1_1Apache_1_1Qpid_1_1Messaging_1_1FailoverUpdates.html", null ],
      [ "Org::Apache::Qpid::Messaging::SessionReceiver::ISessionReceiver", "interfaceOrg_1_1Apache_1_1Qpid_1_1Messaging_1_1SessionReceiver_1_1ISessionReceiver.html", null ],
      [ "Org::Apache::Qpid::Messaging::Message", "classOrg_1_1Apache_1_1Qpid_1_1Messaging_1_1Message.html", null ],
      [ "Org::Apache::Qpid::Messaging::QpidException", "classOrg_1_1Apache_1_1Qpid_1_1Messaging_1_1QpidException.html", null ],
      [ "Org::Apache::Qpid::Messaging::QpidMarshal", "classOrg_1_1Apache_1_1Qpid_1_1Messaging_1_1QpidMarshal.html", null ],
      [ "Org::Apache::Qpid::Messaging::Receiver", "classOrg_1_1Apache_1_1Qpid_1_1Messaging_1_1Receiver.html", null ],
      [ "qpid::messaging::ReceiverImpl", "classqpid_1_1messaging_1_1ReceiverImpl.html", null ],
      [ "Org::Apache::Qpid::Messaging::sealed", "classOrg_1_1Apache_1_1Qpid_1_1Messaging_1_1sealed.html", null ],
      [ "Org::Apache::Qpid::Messaging::Sender", "classOrg_1_1Apache_1_1Qpid_1_1Messaging_1_1Sender.html", null ],
      [ "qpid::messaging::SenderImpl", "classqpid_1_1messaging_1_1SenderImpl.html", null ],
      [ "Org::Apache::Qpid::Messaging::Session", "classOrg_1_1Apache_1_1Qpid_1_1Messaging_1_1Session.html", null ],
      [ "qpid::messaging::SessionImpl", "classqpid_1_1messaging_1_1SessionImpl.html", null ]
    ] ],
    [ "Class Index", "classes.html", null ],
    [ "Class Members", "functions.html", null ],
    [ "Namespace List", "namespaces.html", [
      [ "Org", "namespaceOrg.html", null ],
      [ "Org::Apache", "namespaceOrg_1_1Apache.html", null ],
      [ "Org::Apache::Qpid", "namespaceOrg_1_1Apache_1_1Qpid.html", null ],
      [ "Org::Apache::Qpid::Messaging", "namespaceOrg_1_1Apache_1_1Qpid_1_1Messaging.html", null ],
      [ "Org.Apache.Qpid.Messaging.SessionReceiver", "namespaceOrg_1_1Apache_1_1Qpid_1_1Messaging_1_1SessionReceiver.html", null ],
      [ "qpid", "namespaceqpid.html", null ],
      [ "qpid::messaging", "namespaceqpid_1_1messaging.html", null ]
    ] ],
    [ "Namespace Members", "namespacemembers.html", null ],
    [ "File List", "files.html", [
      [ "Address.cpp", "Address_8cpp.html", null ],
      [ "Address.h", "Address_8h.html", null ],
      [ "AssemblyInfo.cpp", "AssemblyInfo_8cpp.html", null ],
      [ "Connection.cpp", "Connection_8cpp.html", null ],
      [ "Connection.h", "Connection_8h.html", null ],
      [ "Duration.h", "Duration_8h.html", null ],
      [ "FailoverUpdates.cpp", "FailoverUpdates_8cpp.html", null ],
      [ "FailoverUpdates.h", "FailoverUpdates_8h.html", null ],
      [ "Message.cpp", "Message_8cpp.html", null ],
      [ "Message.h", "Message_8h.html", null ],
      [ "QpidException.h", "QpidException_8h.html", null ],
      [ "QpidMarshal.h", "QpidMarshal_8h.html", null ],
      [ "QpidTypeCheck.h", "QpidTypeCheck_8h.html", null ],
      [ "Receiver.cpp", "Receiver_8cpp.html", null ],
      [ "Receiver.h", "Receiver_8h.html", null ],
      [ "resource1.h", "resource1_8h.html", null ],
      [ "Sender.cpp", "Sender_8cpp.html", null ],
      [ "Sender.h", "Sender_8h.html", null ],
      [ "Session.cpp", "Session_8cpp.html", null ],
      [ "Session.h", "Session_8h.html", null ],
      [ "TypeTranslator.cpp", "TypeTranslator_8cpp.html", null ],
      [ "TypeTranslator.h", "TypeTranslator_8h.html", null ],
      [ "sessionreceiver/sessionreceiver.cs", "sessionreceiver_8cs.html", null ],
      [ "sessionreceiver/Properties/sessionreceiver-AssemblyInfo-template.cs", "sessionreceiver-AssemblyInfo-template_8cs.html", null ]
    ] ]
  ] ]
];

function createIndent(o,domNode,node,level)
{
  if (node.parentNode && node.parentNode.parentNode)
  {
    createIndent(o,domNode,node.parentNode,level+1);
  }
  var imgNode = document.createElement("img");
  if (level==0 && node.childrenData)
  {
    node.plus_img = imgNode;
    node.expandToggle = document.createElement("a");
    node.expandToggle.href = "javascript:void(0)";
    node.expandToggle.onclick = function() 
    {
      if (node.expanded) 
      {
        $(node.getChildrenUL()).slideUp("fast");
        if (node.isLast)
        {
          node.plus_img.src = node.relpath+"ftv2plastnode.png";
        }
        else
        {
          node.plus_img.src = node.relpath+"ftv2pnode.png";
        }
        node.expanded = false;
      } 
      else 
      {
        expandNode(o, node, false);
      }
    }
    node.expandToggle.appendChild(imgNode);
    domNode.appendChild(node.expandToggle);
  }
  else
  {
    domNode.appendChild(imgNode);
  }
  if (level==0)
  {
    if (node.isLast)
    {
      if (node.childrenData)
      {
        imgNode.src = node.relpath+"ftv2plastnode.png";
      }
      else
      {
        imgNode.src = node.relpath+"ftv2lastnode.png";
        domNode.appendChild(imgNode);
      }
    }
    else
    {
      if (node.childrenData)
      {
        imgNode.src = node.relpath+"ftv2pnode.png";
      }
      else
      {
        imgNode.src = node.relpath+"ftv2node.png";
        domNode.appendChild(imgNode);
      }
    }
  }
  else
  {
    if (node.isLast)
    {
      imgNode.src = node.relpath+"ftv2blank.png";
    }
    else
    {
      imgNode.src = node.relpath+"ftv2vertline.png";
    }
  }
  imgNode.border = "0";
}

function newNode(o, po, text, link, childrenData, lastNode)
{
  var node = new Object();
  node.children = Array();
  node.childrenData = childrenData;
  node.depth = po.depth + 1;
  node.relpath = po.relpath;
  node.isLast = lastNode;

  node.li = document.createElement("li");
  po.getChildrenUL().appendChild(node.li);
  node.parentNode = po;

  node.itemDiv = document.createElement("div");
  node.itemDiv.className = "item";

  node.labelSpan = document.createElement("span");
  node.labelSpan.className = "label";

  createIndent(o,node.itemDiv,node,0);
  node.itemDiv.appendChild(node.labelSpan);
  node.li.appendChild(node.itemDiv);

  var a = document.createElement("a");
  node.labelSpan.appendChild(a);
  node.label = document.createTextNode(text);
  a.appendChild(node.label);
  if (link) 
  {
    a.href = node.relpath+link;
  } 
  else 
  {
    if (childrenData != null) 
    {
      a.className = "nolink";
      a.href = "javascript:void(0)";
      a.onclick = node.expandToggle.onclick;
      node.expanded = false;
    }
  }

  node.childrenUL = null;
  node.getChildrenUL = function() 
  {
    if (!node.childrenUL) 
    {
      node.childrenUL = document.createElement("ul");
      node.childrenUL.className = "children_ul";
      node.childrenUL.style.display = "none";
      node.li.appendChild(node.childrenUL);
    }
    return node.childrenUL;
  };

  return node;
}

function showRoot()
{
  var headerHeight = $("#top").height();
  var footerHeight = $("#nav-path").height();
  var windowHeight = $(window).height() - headerHeight - footerHeight;
  navtree.scrollTo('#selected',0,{offset:-windowHeight/2});
}

function expandNode(o, node, imm)
{
  if (node.childrenData && !node.expanded) 
  {
    if (!node.childrenVisited) 
    {
      getNode(o, node);
    }
    if (imm)
    {
      $(node.getChildrenUL()).show();
    } 
    else 
    {
      $(node.getChildrenUL()).slideDown("fast",showRoot);
    }
    if (node.isLast)
    {
      node.plus_img.src = node.relpath+"ftv2mlastnode.png";
    }
    else
    {
      node.plus_img.src = node.relpath+"ftv2mnode.png";
    }
    node.expanded = true;
  }
}

function getNode(o, po)
{
  po.childrenVisited = true;
  var l = po.childrenData.length-1;
  for (var i in po.childrenData) 
  {
    var nodeData = po.childrenData[i];
    po.children[i] = newNode(o, po, nodeData[0], nodeData[1], nodeData[2],
        i==l);
  }
}

function findNavTreePage(url, data)
{
  var nodes = data;
  var result = null;
  for (var i in nodes) 
  {
    var d = nodes[i];
    if (d[1] == url) 
    {
      return new Array(i);
    }
    else if (d[2] != null) // array of children
    {
      result = findNavTreePage(url, d[2]);
      if (result != null) 
      {
        return (new Array(i).concat(result));
      }
    }
  }
  return null;
}

function initNavTree(toroot,relpath)
{
  var o = new Object();
  o.toroot = toroot;
  o.node = new Object();
  o.node.li = document.getElementById("nav-tree-contents");
  o.node.childrenData = NAVTREE;
  o.node.children = new Array();
  o.node.childrenUL = document.createElement("ul");
  o.node.getChildrenUL = function() { return o.node.childrenUL; };
  o.node.li.appendChild(o.node.childrenUL);
  o.node.depth = 0;
  o.node.relpath = relpath;

  getNode(o, o.node);

  o.breadcrumbs = findNavTreePage(toroot, NAVTREE);
  if (o.breadcrumbs == null)
  {
    o.breadcrumbs = findNavTreePage("index.html",NAVTREE);
  }
  if (o.breadcrumbs != null && o.breadcrumbs.length>0)
  {
    var p = o.node;
    for (var i in o.breadcrumbs) 
    {
      var j = o.breadcrumbs[i];
      p = p.children[j];
      expandNode(o,p,true);
    }
    p.itemDiv.className = p.itemDiv.className + " selected";
    p.itemDiv.id = "selected";
    $(window).load(showRoot);
  }
}

