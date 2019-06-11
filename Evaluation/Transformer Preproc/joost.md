id: 400

Code snippet:
```
public void handleButton2Request(RequestInvocationEvent event){
  backTrail();
  ServerSiteViewBean vb=(ServerSiteViewBean)getViewBean(ServerSiteViewBean.class);
  passPgSessionMap(vb);
  vb.forwardTo(getRequestContext());
}
```
Comment:
```
This method is called when a request is received.
```
---
id: 401

Code snippet:
```
public boolean isAuthOption(String opt){
  return opt.equals(AccessManagerConstants.ARGUMENT_ADMIN_ID) || opt.equals(AccessManagerConstants.ARGUMENT_PASSWORD_FILE);
}
```
Comment:
```
Returns true if the given option is set.
```
---
id: 402

Code snippet:
```
public ZipException(){
  super();
}
```
Comment:
```
Constructs a <code>zipexception</code> with <code>null</code> as its error detail message.
```
---
id: 403

Code snippet:
```
public AuthenticationInfoList(){
  super(AuthenticationInfo.class,AuthenticationInfoHeader.NAME);
}
```
Comment:
```
Constructs a new exception with <code>null</code> as its detail message. the cause is not initialized.
```
---
id: 404

Code snippet:
```
public NodeSorter(XPathContext p){
  m_execContext=p;
}
```
Comment:
```
Construct a nodesorter, passing in the xsl transformerfactory so it can know how to get the node data according to the proper whitespace rules.
```
---
id: 405

Code snippet:
```
public Builder removeName(final String name){
  names.remove(name);
  return this;
}
```
Comment:
```
Removes the provided user friendly name.
```
---
id: 406

Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(documentimportnode02.class,args);
}
```
Comment:
```
Runs this test from the command line.
```
---
id: 407

Code snippet:
```
public String toString(){
  return actionName + \"=\" + values;
}
```
Comment:
```
Returns the tip text for this property.
```
---
id: 408

Code snippet:
```
public SoundException(final Throwable cause){
  super(cause);
}
```
Comment:
```
Instantiates a new sound exception.
```
---
id: 409

Code snippet:
```
public boolean isFullCompression(){
  return properties.isFullCompression != null ? (boolean)properties.isFullCompression : false;
}
```
Comment:
```
Returns <code>true</code>.
```
---
id: 410

Code snippet:
```
void appendComment(int m_char_current_start,int contentLength){
  int w0=COMMENT_NODE;
  int w1=currentParent;
  int w2=m_char_current_start;
  int w3=contentLength;
  int ourslot=appendNode(w0,w1,w2,w3);
  previousSibling=ourslot;
}
```
Comment:
```
Append a comment child at the current insertion point. assumes that the actual content of the comment has previously been appended to the m_char buffer (shared with the builder).
```
---
id: 411

Code snippet:
```
public int next(){
  int next=_currentNode;
  int pos=--m_ancestorsPos;
  _currentNode=(pos >= 0) ? m_ancestors[m_ancestorsPos] : DTM.NULL;
  return returnNode(next);
}
```
Comment:
```
Get the next node in the iteration.
```
---
id: 412

Code snippet:
```
public void disable(){
  state.save();
  state.clearInMemory();
  disabled=true;
  disableService();
}
```
Comment:
```
Disables the memory cache.
```
---
id: 413

Code snippet:
```
public String[] processName(String qName,String[] parts,boolean isAttribute){
  String[] name=currentContext.processName(qName,isAttribute);
  if (name == null)   return null;
  System.arraycopy(name,0,parts,0,3);
  return parts;
}
```
Comment:
```
Processes an attribute.
```
---
id: 414

Code snippet:
```
@Override public long dynamicQueryCount(DynamicQuery dynamicQuery,Projection projection){
  return fooPersistence.countWithDynamicQuery(dynamicQuery,projection);
}
```
Comment:
```
Returns the number of rows matching the dynamic query.
```
---
id: 415

Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  NodeList elementList;
  Element testAddr;
  Attr addrAttr;
  int nodeType;
  doc=(Document)load(\"hc_staff\",false);
  elementList=doc.getElementsByTagName(\"acronym\");
  testAddr=(Element)elementList.item(0);
  addrAttr=testAddr.getAttributeNode(\"title\");
  nodeType=(int)addrAttr.getNodeType();
  assertEquals(\"nodeAttrNodeTypeAssert1\",2,nodeType);
}
```
Comment:
```
Runs the test case.
```
---
id: 416

Code snippet:
```
public boolean isBuiltIn(){
  return builtIn;
}
```
Comment:
```
Returns true if this is a variable.
```
---
id: 417

Code snippet:
```
String constructComponentName(){
synchronized (List.class) {
    return base + nameCounter++;
  }
}
```
Comment:
```
Returns the name of the component.
```
---
id: 418

Code snippet:
```
public static void access(Level level,String msgid,String data[],Object session,Map props){
  if (logger != null) {
    try {
      logger.access(level,msgid,data,session,props);
    }
 catch (    LogException le) {
      SAML2Utils.debug.error(\"LogUtil.access: Couldn\'t write log:\",le);
    }
  }
}
```
Comment:
```
Logs message to saml2 access logs.
```
---
id: 419

Code snippet:
```
protected ASN1TypeCollection(int tagNumber,ASN1Type[] type){
  super(tagNumber);
  this.type=type;
  this.OPTIONAL=new boolean[type.length];
  this.DEFAULT=new Object[type.length];
}
```
Comment:
```
Constructs asn.1 collection type.
```
---
id: 420

Code snippet:
```
public ResponseProviderTypeManager(PolicyManager pm){
  this.pm=pm;
  token=pm.token;
  java.util.Locale loc;
  try {
    String lstr=token.getProperty(\"Locale\");
    loc=com.sun.identity.shared.locale.Locale.getLocale(lstr);
  }
 catch (  SSOException ex) {
    debug.error(\"ResponseProviderTypeManager:Unable to retreive \" + \"locale from SSOToken\",ex);
    loc=Locale.getDefaultLocale();
  }
  if (debug.messageEnabled()) {
    debug.message(\"ResponseProviderTypeManager locale=\" + loc + \"\tI18nFileName = \"+ ResBundleUtils.rbName);
  }
  rb=amCache.getResBundle(ResBundleUtils.rbName,loc);
}
```
Comment:
```
Constructs a <code>responseprovidertypemanager</code> object.
```
---
id: 421

Code snippet:
```
public PropertyValueEditor(ConsoleApplication app,ManagementContext context){
  this.app=app;
  this.context=context;
}
```
Comment:
```
Creates a new instance.
```
---
id: 422

Code snippet:
```
public void consume(){
  consumed=true;
}
```
Comment:
```
Consumes this event so that it will not be processed in the default manner by the source which originated it.
```
---
id: 423

Code snippet:
```
public PWResetSuccessModelImpl(){
  super();
}
```
Comment:
```
Creates a new instance.
```
---
id: 424

Code snippet:
```
protected BooleanControl(Type type,boolean initialValue){
  this(type,initialValue,\"true\",\"false\");
}
```
Comment:
```
Constructs a new boolean control object with the given parameters. the labels for the <code>true</code> and <code>false</code> states default to \"true\" and \"false.\".
```
---
id: 425

Code snippet:
```
public void clear(){
  Arrays.fill(elements,0);
  size=0;
}
```
Comment:
```
Removes all of the elements from this list. the list will be empty after this call returns.
```
---
id: 426

Code snippet:
```
public void startElement(StylesheetHandler handler,String uri,String localName,String rawName,Attributes attributes) throws org.xml.sax.SAXException {
  Stylesheet thisSheet=handler.getStylesheet();
  WhitespaceInfoPaths paths=new WhitespaceInfoPaths(thisSheet);
  setPropertiesFromAttributes(handler,rawName,attributes,paths);
  Vector xpaths=paths.getElements();
  for (int i=0; i < xpaths.size(); i++) {
    WhiteSpaceInfo wsi=new WhiteSpaceInfo((XPath)xpaths.elementAt(i),true,thisSheet);
    wsi.setUid(handler.nextUid());
    thisSheet.setStripSpaces(wsi);
  }
  paths.clearElements();
}
```
Comment:
```
Receive notification of the start of an element.
```
---
id: 427

Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  NodeList elementList;
  Node docNode;
  Document ownerDocument;
  Element docElement;
  String elementName;
  doc=(Document)load(\"staff\",false);
  elementList=doc.getElementsByTagName(\"employee\");
  docNode=elementList.item(1);
  ownerDocument=docNode.getOwnerDocument();
  docElement=ownerDocument.getDocumentElement();
  elementName=docElement.getNodeName();
  if ((\"image/svg+xml\".equals(getContentType()))) {
    assertEquals(\"svgTagName\",\"svg\",elementName);
  }
 else {
    assertEquals(\"nodeGetOwnerDocumentAssert1\",\"staff\",elementName);
  }
}
```
Comment:
```
Runs the test case.
```
---
id: 428

Code snippet:
```
@Override public String toString(){
  String dsc=null;
switch (this.type) {
case TYPE_UNDERFLOW:
    dsc=\"UNDERFLOW error\";
  break;
case TYPE_OVERFLOW:
dsc=\"OVERFLOW error\";
break;
case TYPE_UNMAPPABLE_CHAR:
dsc=\"Unmappable-character error with erroneous input length \" + this.length;
break;
case TYPE_MALFORMED_INPUT:
dsc=\"Malformed-input error with erroneous input length \" + this.length;
break;
default :
dsc=\"\";
break;
}
return getClass().getName() + \"[\" + dsc+ \"]\";
}
```
Comment:
```
Returns a text description of this result.
```
---
id: 429

Code snippet:
```
void reset(Component owner,Component contents,int ownerX,int ownerY){
  super.reset(owner,contents,ownerX,ownerY);
  JComponent component=(JComponent)getComponent();
  component.setOpaque(contents.isOpaque());
  component.setLocation(ownerX,ownerY);
  component.add(contents,BorderLayout.CENTER);
  contents.invalidate();
  pack();
}
```
Comment:
```
Resets the <code>popup</code> to an initial state.
```
---
id: 430

Code snippet:
```
public static int readUBEInt24(ByteBuffer b){
  int result=0;
  result+=readUBEInt16(b) << 16;
  result+=readUInt8(b);
  return result;
}
```
Comment:
```
Read an unsigned big-endian 24-bit integer using an nio bytebuffer.
```
---
id: 431

Code snippet:
```
private boolean doesMatch(String pattern,int pp,String result,int rp){
  for (; ; ) {
    if (pp == pattern.length() && rp == result.length())     return true;
    if (pp == pattern.length())     return false;
    char pc=pattern.charAt(pp);
    if (pc == \'_\') {
      if (rp == result.length())       return false;
      pp++;
      rp++;
    }
 else     if (pc == \'%\') {
      if (pp == pattern.length() - 1) {
        return true;
      }
      for (int sp=rp; sp < result.length(); sp++) {
        if (doesMatch(pattern,pp + 1,result,sp)) {
          return true;
        }
      }
      return false;
    }
 else {
      if (rp == result.length())       return false;
      if (pc != result.charAt(rp)) {
        return false;
      }
      pp++;
      rp++;
    }
  }
}
```
Comment:
```
Returns true if the given string matches the pattern.
```
---
id: 432

Code snippet:
```
public FieldPosition(Format.Field attribute){
  this(attribute,-1);
}
```
Comment:
```
Creates a fieldposition object for the given field constant. fields are identified by constants defined in the various <code>format</code> subclasses. this is equivalent to calling <code>new fieldposition(attribute, -1)</code>.
```
---
id: 433

Code snippet:
```
public void testParseLargestSubnormalDoublePrecision(){
  assertEquals(2.2250738585072014E-308,Double.parseDouble(\"2.2250738585072012e-308\"));
  assertEquals(2.2250738585072014E-308,Double.parseDouble(\"0.00022250738585072012e-304\"));
  assertEquals(2.2250738585072014E-308,Double.parseDouble(\"00000002.2250738585072012e-308\"));
  assertEquals(2.2250738585072014E-308,Double.parseDouble(\"2.225073858507201200000e-308\"));
  assertEquals(2.2250738585072014E-308,Double.parseDouble(\"2.2250738585072012e-00308\"));
  assertEquals(2.2250738585072014E-308,Double.parseDouble(\"2.22507385850720129978001e-308\"));
  assertEquals(-2.2250738585072014E-308,Double.parseDouble(\"-2.2250738585072012e-308\"));
}
```
Comment:
```
This value has been known to cause javac and java to infinite loop. http://www.exploringbinary.com/java-hangs-when-converting-2-2250738585072012e-308/.
```
---
id: 434

Code snippet:
```
public int lastIndexOf(String string){
  return lastIndexOf(string,count);
}
```
Comment:
```
Searches for the last index of the specified character. the search for the character starts at the end and moves towards the beginning.
```
---
id: 435

Code snippet:
```
public static int copy(Reader input,Writer output) throws IOException {
  long count=copyLarge(input,output);
  if (count > Integer.MAX_VALUE) {
    return -1;
  }
  return (int)count;
}
```
Comment:
```
Copy chars from a <code>reader</code> to a <code>writer</code>. <p> this method buffers the input internally, so there is no need to use a <code>bufferedreader</code>. <p> large streams (over 2gb) will return a chars copied value of <code>-1</code> after the copy has completed since the correct number of chars cannot be returned as an int. for large streams use the <code>copylarge(reader, writer)</code> method.
```
---
id: 436

Code snippet:
```
@RequestMapping(value=\"/authenticate\",method=RequestMethod.GET,produces=MediaType.APPLICATION_JSON_VALUE) @Timed public String isAuthenticated(HttpServletRequest request){
  log.debug(\"REST request to check if the current user is authenticated\");
  return request.getRemoteUser();
}
```
Comment:
```
Post /users -> create a new user.
```
---
id: 437

Code snippet:
```
private Node tryAppend(Node s,boolean haveData){
  for (Node t=tail, p=t; ; ) {
    Node n, u;
    if (p == null && (p=head) == null) {
      if (casHead(null,s))       return s;
    }
 else     if (p.cannotPrecede(haveData))     return null;
 else     if ((n=p.next) != null)     p=p != t && t != (u=tail) ? (t=u) : (p != n) ? n : null;
 else     if (!p.casNext(null,s))     p=p.next;
 else {
      if (p != t) {
        while ((tail != t || !casTail(t,s)) && (t=tail) != null && (s=t.next) != null && (s=s.next) != null && s != t)         ;
      }
      return p;
    }
  }
}
```
Comment:
```
Tries to append node s as tail.
```
---
id: 438

Code snippet:
```
public PopupMenuEvent(Object source){
  super(source);
}
```
Comment:
```
Creates a new <code>popupevent</code> object.
```
---
id: 439

Code snippet:
```
public final void append(char value){
  char[] chunk;
  if (m_firstFree < m_chunkSize)   chunk=m_array[m_lastChunk];
 else {
    int i=m_array.length;
    if (m_lastChunk + 1 == i) {
      char[][] newarray=new char[i + 16][];
      System.arraycopy(m_array,0,newarray,0,i);
      m_array=newarray;
    }
    chunk=m_array[++m_lastChunk];
    if (chunk == null) {
      if (m_lastChunk == 1 << m_rebundleBits && m_chunkBits < m_maxChunkBits) {
        m_innerFSB=new FastStringBuffer(this);
      }
      chunk=m_array[m_lastChunk]=new char[m_chunkSize];
    }
    m_firstFree=0;
  }
  chunk[m_firstFree++]=value;
}
```
Comment:
```
Appends <code>len</code> bytes to buffer.
```
---
id: 440

Code snippet:
```
public static boolean isLECPProfile(HttpServletRequest request){
  java.util.Enumeration headerNames=request.getHeaderNames();
  while (headerNames.hasMoreElements()) {
    String hn=headerNames.nextElement().toString();
    String hv=request.getHeader(hn);
    if (FSUtils.debug.messageEnabled()) {
      FSUtils.debug.message(\"header \" + hn + \" val \"+ hv);
    }
  }
  String lecpHeaderValue=(String)request.getHeader(IFSConstants.LECP_HEADER_NAME);
  if (FSUtils.debug.messageEnabled()) {
    FSUtils.debug.message(\" value of lecp in header \" + lecpHeaderValue);
  }
  if (lecpHeaderValue == null) {
    lecpHeaderValue=(String)request.getHeader((IFSConstants.LECP_HEADER_NAME).toLowerCase());
  }
  if (lecpHeaderValue != null) {
    return true;
  }
 else {
    return false;
  }
}
```
Comment:
```
Determines whether the request contains lecp header or not.
```
---
id: 441

Code snippet:
```
public boolean removeAll(Collection c){
  throw new UnsupportedOperationException();
}
```
Comment:
```
Remove all specified children (unsupported) implementations must synchronized on the hierarchy lock and \"children\" protected field.
```
---
id: 442

Code snippet:
```
public boolean isServiceVisible(String serviceName){
  return !CollectionUtils.isEmpty(hiddenServices) && !hiddenServices.contains(serviceName);
}
```
Comment:
```
Returns true if the provided service name is not in the list of hidden services.
```
---
id: 443

Code snippet:
```
public void removeServiceConfig(String serviceName) throws SMSException {
  try {
    ServiceConfigManager scm=new ServiceConfigManager(serviceName,token);
    scm.deleteOrganizationConfig(orgName);
  }
 catch (  SSOException ssoe) {
    SMSEntry.debug.error(\"OrganizationConfigManager: Unable to \" + \"delete Service Config\",ssoe);
    throw (new SMSException(SMSEntry.bundle.getString(SMS_INVALID_SSO_TOKEN),SMS_INVALID_SSO_TOKEN));
  }
}
```
Comment:
```
Removes a service.
```
---
id: 444

Code snippet:
```
public boolean isDocOrdered(){
  return m_exprObj.isDocOrdered();
}
```
Comment:
```
Returns true if all the nodes in the iteration well be returned in document order. warning: this can only be called after setroot has been called!.
```
---
id: 445

Code snippet:
```
public static SQLiteConnectionPool open(SQLiteDatabaseConfiguration configuration){
  if (configuration == null) {
    throw new IllegalArgumentException(\"configuration must not be null.\");
  }
  SQLiteConnectionPool pool=new SQLiteConnectionPool(configuration);
  pool.open();
  return pool;
}
```
Comment:
```
Opens a connection to the database.
```
---
id: 446

Code snippet:
```
@Override public boolean accept(ClusterMessage msg){
  return (msg instanceof FileMessage) || (msg instanceof UndeployMessage);
}
```
Comment:
```
Returns true if the given message is an error.
```
---
id: 447

Code snippet:
```
public void performPostDelete(ServerManagedObject<?> managedObject) throws ConfigException {
}
```
Comment:
```
Performs any post-delete processing required by this constraint. this method is invoked after a managed object has been accepted for deletion from the server\'s configuration. <p> the default implementation is to do nothing.
```
---
id: 448

Code snippet:
```
public ArrayDeque<E> clone(){
  try {
    @SuppressWarnings(\"unchecked\") ArrayDeque<E> result=(ArrayDeque<E>)super.clone();
    result.elements=Arrays.copyOf(elements,elements.length);
    return result;
  }
 catch (  CloneNotSupportedException e) {
    throw new AssertionError();
  }
}
```
Comment:
```
Returns a copy of this deque.
```
---
id: 449

Code snippet:
```
public Set createSubOrganizationalUnits(Map subOrganizationalUnitsMap) throws AMException, SSOException {
  Iterator iter=subOrganizationalUnitsMap.keySet().iterator();
  Set subOrgUnits=new HashSet();
  while (iter.hasNext()) {
    String subOrgUnitName=(String)iter.next();
    String subOrgUnitDN=AMNamingAttrManager.getNamingAttr(ORGANIZATIONAL_UNIT) + \"=\" + subOrgUnitName+ \",\"+ super.entryDN;
    Map attributes=(Map)subOrganizationalUnitsMap.get(subOrgUnitName);
    AMOrganizationalUnitImpl subOrgUnitImpl=new AMOrganizationalUnitImpl(super.token,subOrgUnitDN);
    subOrgUnitImpl.setAttributes(attributes);
    subOrgUnitImpl.create();
    subOrgUnits.add(subOrgUnitImpl);
  }
  return subOrgUnits;
}
```
Comment:
```
Creates sub-organizational units and initializes their attributes.
```
---
id: 450

Code snippet:
```
public void processBye(RequestEvent requestEvent,ServerTransaction serverTransactionId){
  Request request=requestEvent.getRequest();
  try {
    System.out.println(\"shootme:  got a bye sending OK.\");
    Response response=messageFactory.createResponse(200,request,null,null);
    serverTransactionId.sendResponse(response);
    System.out.println(\"Dialog State is \" + serverTransactionId.getDialog().getState());
  }
 catch (  Exception ex) {
    ex.printStackTrace();
    System.exit(0);
  }
}
```
Comment:
```
Processes a response.
```
---
id: 451

Code snippet:
```
public StringHashMap(String identifier,AbstractTagFrameBody frameBody,int size){
  super(identifier,frameBody,size);
  if (identifier.equals(DataTypes.OBJ_LANGUAGE)) {
    valueToKey=Languages.getInstanceOf().getValueToIdMap();
    keyToValue=Languages.getInstanceOf().getIdToValueMap();
  }
 else {
    throw new IllegalArgumentException(\"Hashmap identifier not defined in this class: \" + identifier);
  }
}
```
Comment:
```
Creates a new timingspecifier object.
```
---
id: 452

Code snippet:
```
public void initObjectGraph(Object module){
  mObjectGraph=module != null ? ObjectGraph.create(module) : null;
}
```
Comment:
```
Initialize the graph from the given graph.
```
---
id: 453

Code snippet:
```
public int hashCode(){
  return uid.hashCode();
}
```
Comment:
```
Returns a hash code for this instance.
```
---
id: 454

Code snippet:
```
public void installUI(JComponent a){
  for (int i=0; i < uis.size(); i++) {
    ((ComponentUI)(uis.elementAt(i))).installUI(a);
  }
}
```
Comment:
```
Invokes the <code>installui</code> method on each ui handled by this object.
```
---
id: 455

Code snippet:
```
public org.omg.CORBA.TypeCode type(){
  org.omg.CORBA.portable.ServantObject $so=_servant_preinvoke(\"type\",_opsClass);
  DynStructOperations $self=(DynStructOperations)$so.servant;
  try {
    return $self.type();
  }
  finally {
    _servant_postinvoke($so);
  }
}
```
Comment:
```
Returns a new instance of this class.
```
---
id: 456

Code snippet:
```
LogReaderPool(File file,RecordParser<K,V> parser){
  this.file=file;
  this.parser=parser;
}
```
Comment:
```
Creates a new <code>logrecordreader</code> instance.
```
---
id: 457

Code snippet:
```
public void abortAnimation(){
  finished=true;
  currentMaxY=endMaxY;
}
```
Comment:
```
Ignore repeat events.
```
---
id: 458

Code snippet:
```
public String toXMLString(boolean includeNSPrefix,boolean declareNS) throws SAML2Exception {
  String xmlStr=null;
  if ((extensionsList != null) && (!extensionsList.isEmpty())) {
    StringBuffer xmlString=new StringBuffer(500);
    xmlString.append(SAML2Constants.START_TAG);
    if (includeNSPrefix) {
      xmlString.append(SAML2Constants.PROTOCOL_PREFIX);
    }
    xmlString.append(SAML2Constants.EXTENSIONS);
    if (declareNS) {
      xmlString.append(SAML2Constants.PROTOCOL_DECLARE_STR);
    }
    xmlString.append(SAML2Constants.END_TAG);
    Iterator extIterator=extensionsList.iterator();
    while (extIterator.hasNext()) {
      String extString=(String)extIterator.next();
      xmlString.append(SAML2Constants.NEWLINE).append(extString);
    }
    xmlString.append(SAML2Constants.NEWLINE).append(SAML2Constants.SAML2_END_TAG).append(SAML2Constants.EXTENSIONS).append(SAML2Constants.END_TAG);
    xmlStr=xmlString.toString();
  }
  return xmlStr;
}
```
Comment:
```
Returns a string representation of this object.
```
---
id: 459

Code snippet:
```
public Policy(String policyName) throws InvalidNameException {
  this(policyName,null);
}
```
Comment:
```
Constructs a policy given the policy name.
```
---
id: 460

Code snippet:
```
public void initializeSASLMechanismHandlers() throws ConfigException, InitializationException {
  RootCfg rootConfiguration=serverContext.getRootConfig();
  rootConfiguration.addSASLMechanismHandlerAddListener(this);
  rootConfiguration.addSASLMechanismHandlerDeleteListener(this);
  for (  String handlerName : rootConfiguration.listSASLMechanismHandlers()) {
    SASLMechanismHandlerCfg handlerConfiguration=rootConfiguration.getSASLMechanismHandler(handlerName);
    handlerConfiguration.addChangeListener(this);
    if (handlerConfiguration.isEnabled()) {
      String className=handlerConfiguration.getJavaClass();
      try {
        SASLMechanismHandler handler=loadHandler(className,handlerConfiguration,true);
        handlers.put(handlerConfiguration.dn(),handler);
      }
 catch (      InitializationException ie) {
        logger.error(ie.getMessageObject());
        continue;
      }
    }
  }
}
```
Comment:
```
Initializes all sasl mechanism handlers currently defined in the directory server configuration. this should only be called at directory server startup.
```
---
id: 461

Code snippet:
```
public static FastJsonConverterFactory create(){
  return new FastJsonConverterFactory();
}
```
Comment:
```
Creates a new instance of this class.
```
---
id: 462

Code snippet:
```
public static ByteBuffer isXingFrame(ByteBuffer bb,MPEGFrameHeader mpegFrameHeader){
  int startPosition=bb.position();
  if (mpegFrameHeader.getVersion() == MPEGFrameHeader.VERSION_1) {
    if (mpegFrameHeader.getChannelMode() == MPEGFrameHeader.MODE_MONO) {
      bb.position(startPosition + MPEG_VERSION_1_MODE_MONO_OFFSET);
    }
 else {
      bb.position(startPosition + MPEG_VERSION_1_MODE_STEREO_OFFSET);
    }
  }
 else {
    if (mpegFrameHeader.getChannelMode() == MPEGFrameHeader.MODE_MONO) {
      bb.position(startPosition + MPEG_VERSION_2_MODE_MONO_OFFSET);
    }
 else {
      bb.position(startPosition + MPEG_VERSION_2_MODE_STEREO_OFFSET);
    }
  }
  ByteBuffer header=bb.slice();
  bb.position(startPosition);
  byte[] identifier=new byte[XING_IDENTIFIER_BUFFER_SIZE];
  header.get(identifier);
  if ((!Arrays.equals(identifier,XING_VBR_ID)) && (!Arrays.equals(identifier,XING_CBR_ID))) {
    return null;
  }
  MP3File.logger.finest(\"Found Xing Frame\");
  return header;
}
```
Comment:
```
Is this a xing frame.
```
---
id: 463

Code snippet:
```
public void makeImmutable(){
  if (isMutable) {
    isMutable=false;
  }
}
```
Comment:
```
Makes this object immutable.
```
---
id: 464

Code snippet:
```
public boolean equals(Object obj){
  return (this == obj);
}
```
Comment:
```
Indicates whether some other object is \"equal to\" this one.
```
---
id: 465

Code snippet:
```
public ObjectInputStreamWithLoader(InputStream in,ClassLoader loader) throws IOException, StreamCorruptedException {
  super(in);
  if (loader == null) {
    throw new IllegalArgumentException(\"Illegal null argument to ObjectInputStreamWithLoader\");
  }
  this.loader=loader;
}
```
Comment:
```
Loader must be non-null;.
```
---
id: 466

Code snippet:
```
@Override public View create(Element elem){
  return new PasswordView(elem);
}
```
Comment:
```
Creates a view (passwordview) for an element.
```
---
id: 467

Code snippet:
```
public boolean isSingleAttributeContainer(){
  return false;
}
```
Comment:
```
Returns false for the idpplegalidentity container.
```
---
id: 468

Code snippet:
```
public ObjectFactory(){
  super(grammarInfo);
}
```
Comment:
```
Creates a new instance.
```
---
id: 469

Code snippet:
```
public void paint(Graphics a,JComponent b){
  for (int i=0; i < uis.size(); i++) {
    ((ComponentUI)(uis.elementAt(i))).paint(a,b);
  }
}
```
Comment:
```
Invokes the <code>paint</code> method on each ui handled by this object.
```
---
id: 470

Code snippet:
```
public boolean update(Long parameterID,String parameterName,Long actionID,Long dataTypeID){
  if (parameterID == null) {
    throw new IllegalArgumentException(\"primary key null.\");
  }
  ContentValues args=new ContentValues();
  if (parameterName != null) {
    args.put(KEY_ACTIONPARAMETERNAME,parameterName);
  }
  if (actionID != null) {
    args.put(KEY_ACTIONID,actionID);
  }
  if (dataTypeID != null) {
    args.put(KEY_DATATYPEID,dataTypeID);
  }
  if (args.size() > 0) {
    return database.update(DATABASE_TABLE,args,KEY_ACTIONPARAMETERID + \"=\" + parameterID,null) > 0;
  }
  return false;
}
```
Comment:
```
Updates an existing data object.
```
---
id: 471

Code snippet:
```
public void processAck(RequestEvent requestEvent,ServerTransaction serverTransaction){
  System.out.println(\"shootme: got an ACK! \");
  System.out.println(\"Dialog State = \" + dialog.getState());
}
```
Comment:
```
Processes the given event.
```
---
id: 472

Code snippet:
```
@Override public String encodeURL(String url){
  String absolute;
  try {
    absolute=toAbsolute(url);
  }
 catch (  IllegalArgumentException iae) {
    return url;
  }
  if (isEncodeable(absolute)) {
    if (url.equalsIgnoreCase(\"\")) {
      url=absolute;
    }
 else     if (url.equals(absolute) && !hasPath(url)) {
      url+=\'/\';
    }
    return (toEncoded(url,request.getSessionInternal().getIdInternal()));
  }
 else {
    return (url);
  }
}
```
Comment:
```
Encode the session identifier associated with this response into the specified url, if necessary.
```
---
id: 473

Code snippet:
```
public OpenDataException(){
  super();
}
```
Comment:
```
Constructs a new exception with <code>null</code> as its detail message. the cause is not initialized.
```
---
id: 474

Code snippet:
```
public SMSubConfigComparator(Collator collator){
  this.collator=collator;
}
```
Comment:
```
Creates an instance of <code>smsubconfigcomparator</code>.
```
---
id: 475

Code snippet:
```
public void error(SAXParseException e) throws SAXException {
}
```
Comment:
```
Receive notification of a recoverable parser error. <p>the default implementation does nothing. application writers may override this method in a subclass to take specific actions at the end of each warning.</p>.
```
---
id: 476

Code snippet:
```
public void reset(){
  gsStack.removeAllElements();
  gsStack.push(new ParserGraphicsState());
  textMatrix=null;
  textLineMatrix=null;
  resourcesStack=new Stack<>();
  isClip=false;
  currentPath=new Path();
}
```
Comment:
```
Resets the graphics state stack, matrices and resources.
```
---
id: 477

Code snippet:
```
public PlanarYUVLuminanceSource buildLuminanceSource(byte[] data,int width,int height){
  Rect rect=getFramingRectInPreview();
  if (rect == null) {
    return null;
  }
  return new PlanarYUVLuminanceSource(data,width,height,rect.left,rect.top,rect.width(),rect.height(),false);
}
```
Comment:
```
A factory method to build the appropriate luminancesource object based on the format of the preview buffers, as described by camera.parameters.
```
---
id: 478

Code snippet:
```
@Override public void recycle(){
  lock();
  try {
    super.recycle();
    deltaRequest.clear();
  }
  finally {
    unlock();
  }
}
```
Comment:
```
Release all object references, and initialize instance variables, in preparation for reuse of this object.
```
---
id: 479

Code snippet:
```
public IndexModifiedEvent(BackendDescriptor backend){
  this.modifiedIndexes.addAll(backend.getIndexes());
  this.modifiedIndexes.addAll(backend.getVLVIndexes());
}
```
Comment:
```
Creates a new instance.
```
---
id: 480

Code snippet:
```
public void processAck(RequestEvent requestEvent,ServerTransaction serverTransaction){
  SipProvider sipProvider=(SipProvider)requestEvent.getSource();
  try {
    System.out.println(\"shootme: got an ACK \" + requestEvent.getRequest());
  }
 catch (  Exception ex) {
    ex.printStackTrace();
    System.exit(0);
  }
}
```
Comment:
```
Processes this message. this method is invoked by the receiver of the message.
```
---
id: 481

Code snippet:
```
public static boolean isXML11ValidName(String name){
  int length=name.length();
  if (length == 0)   return false;
  int i=1;
  char ch=name.charAt(0);
  if (!isXML11NameStart(ch)) {
    if (length > 1 && isXML11NameHighSurrogate(ch)) {
      char ch2=name.charAt(1);
      if (!XMLChar.isLowSurrogate(ch2) || !isXML11NameStart(XMLChar.supplemental(ch,ch2))) {
        return false;
      }
      i=2;
    }
 else {
      return false;
    }
  }
  while (i < length) {
    ch=name.charAt(i);
    if (!isXML11Name(ch)) {
      if (++i < length && isXML11NameHighSurrogate(ch)) {
        char ch2=name.charAt(i);
        if (!XMLChar.isLowSurrogate(ch2) || !isXML11Name(XMLChar.supplemental(ch,ch2))) {
          return false;
        }
      }
 else {
        return false;
      }
    }
    ++i;
  }
  return true;
}
```
Comment:
```
Check to see if a string is a valid name according to [5] in the xml 1.1 recommendation.
```
---
id: 482

Code snippet:
```
public RefinedSoundex(){
  this(US_ENGLISH_MAPPING);
}
```
Comment:
```
Creates an instance of the refinedsoundex object using the default us english mapping.
```
---
id: 483

Code snippet:
```
public ServiceAlreadyExistsException(){
  super();
}
```
Comment:
```
Constructs a new exception with <code>null</code> as its detail message. the cause is not initialized.
```
---
id: 484

Code snippet:
```
public MethodHandle findSetter(Class<?> refc,String name,Class<?> type) throws NoSuchFieldException, IllegalAccessException {
  MemberName field=resolveOrFail(REF_putField,refc,name,type);
  return getDirectField(REF_putField,refc,field);
}
```
Comment:
```
Produces a method handle giving write access to a non-static field. the type of the method handle will have a void return type. the method handle will take two arguments, the instance containing the field, and the value to be stored. the second argument will be of the field\'s value type. access checking is performed immediately on behalf of the lookup class.
```
---
id: 485

Code snippet:
```
private void savehttpRedLogout(String lohttpLocation,String lohttpRespLocation,List logList,com.sun.identity.saml2.jaxb.metadata.ObjectFactory objFact) throws JAXBException {
  if (lohttpLocation != null && lohttpLocation.length() > 0) {
    SingleLogoutServiceElement slsElemRed=objFact.createSingleLogoutServiceElement();
    slsElemRed.setBinding(httpRedirectBinding);
    slsElemRed.setLocation(lohttpLocation);
    slsElemRed.setResponseLocation(lohttpRespLocation);
    logList.add(slsElemRed);
  }
}
```
Comment:
```
Saves an element to the database.
```
---
id: 486

Code snippet:
```
public void testSecretKeyFactory08() throws NoSuchAlgorithmException {
  if (!DEFSupported) {
    fail(NotSupportMsg);
    return;
  }
  Provider prov=null;
  for (int i=0; i < validValues.length; i++) {
    try {
      SecretKeyFactory.getInstance(validValues[i],prov);
      fail(\"IllegalArgumentException was not thrown as expected (provider is null, algorithm: \".concat(validValues[i]).concat(\")\"));
    }
 catch (    IllegalArgumentException e) {
    }
  }
}
```
Comment:
```
Test for <code>getinstance(string algorithm, string provider)</code> method assertion: throws nullpointerexception when algorithm is null; throws nosuchalgorithmexception when algorithm is not correct;.
```
---
id: 487

Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  NodeList addressList;
  Node testNode;
  NamedNodeMap attributes;
  Attr domesticAttr;
  Node s;
  doc=(Document)load(\"staff\",false);
  addressList=doc.getElementsByTagName(\"address\");
  testNode=addressList.item(0);
  attributes=testNode.getAttributes();
  domesticAttr=(Attr)attributes.getNamedItem(\"domestic\");
  s=domesticAttr.getNextSibling();
  assertNull(\"attrNextSiblingNullAssert\",s);
}
```
Comment:
```
Runs the test case.
```
---
id: 488

Code snippet:
```
private Map<String,Object> buildPatchForPasswords(final List<String> newPasswords) throws JsonCryptoException {
  final Map<String,Object> patchFields=new HashMap<>();
  JsonValue crypto=new JsonCrypto(encryptor.getType(),encryptor.encrypt(new JsonValue(newPasswords.get(0)))).toJsonValue();
switch (compatMode) {
case V2:
    patchFields.put(\"replace\",new JsonPointer(currentConfig.getPasswordAttribute()).toString());
  patchFields.put(\"value\",crypto.asMap());
break;
case V3:
patchFields.put(\"operation\",\"replace\");
patchFields.put(\"field\",new JsonPointer(currentConfig.getPasswordAttribute()).toString());
patchFields.put(\"value\",crypto.asMap());
break;
default :
throw new IllegalArgumentException(\"Unknown compatibility mode: \" + compatMode);
}
return patchFields;
}
```
Comment:
```
Build a map from a set of attributes.
```
---
id: 489

Code snippet:
```
public static void logCompareResponse(CompareOperation compareOperation){
  for (  AccessLogPublisher<?> publisher : getAccessLogPublishers()) {
    publisher.logCompareResponse(compareOperation);
  }
}
```
Comment:
```
Logs requests that took over slow_request_threshold_ms to complete.
```
---
id: 490

Code snippet:
```
public static <T>void removeAll(Collection<T> collection,Collection<T> elements){
  if (CollectionUtils.isEmpty(collection) || CollectionUtils.isEmpty(elements)) {
    return;
  }
  for (  T element : elements) {
    collection.remove(element);
  }
}
```
Comment:
```
Safe method to remove all specified elements from the collection.
```
---
id: 491

Code snippet:
```
void updateIDFFEntityConfig(String realm,String cotName,Set trustedProviders) throws COTException {
  String classMethod=\"COTManager:updateIDFFEntityConfig\";
  IDFFCOTUtils idffCotUtils=new IDFFCOTUtils(callerSession);
  String entityId=null;
  if (trustedProviders != null && !trustedProviders.isEmpty()) {
    for (Iterator iter=trustedProviders.iterator(); iter.hasNext(); ) {
      entityId=(String)iter.next();
      try {
        idffCotUtils.updateEntityConfig(realm,cotName,entityId);
      }
 catch (      IDFFMetaException idfe) {
        throw new COTException(idfe);
      }
catch (      JAXBException jbe) {
        debug.error(classMethod,jbe);
        String[] data={jbe.getMessage(),cotName,entityId,realm};
        LogUtil.error(Level.INFO,LogUtil.CONFIG_ERROR_CREATE_COT_DESCRIPTOR,data);
        throw new COTException(jbe);
      }
    }
  }
}
```
Comment:
```
Updates an existing class.
```
---
id: 492

Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(nodesetprefix07.class,args);
}
```
Comment:
```
Runs this test from the command line.
```
---
id: 493

Code snippet:
```
public void paintTableHeaderBackground(SynthContext context,Graphics g,int x,int y,int w,int h){
}
```
Comment:
```
Paints the background of the header of a table.
```
---
id: 494

Code snippet:
```
protected RemoteObject(){
  ref=null;
}
```
Comment:
```
Creates a remote object.
```
---
id: 495

Code snippet:
```
private void checkInstallStatus() throws InitializationException {
  final CurrentInstallStatus installStatus=new CurrentInstallStatus();
  if (installStatus.canOverwriteCurrentInstall()) {
    if (isInteractive()) {
      println(installStatus.getInstallationMsg());
      try {
        if (!confirmAction(INFO_CLI_DO_YOU_WANT_TO_CONTINUE.get(),true)) {
          throw new InitializationException(LocalizableMessage.EMPTY);
        }
      }
 catch (      final ClientException ce) {
        logger.error(LocalizableMessage.raw(\"Unexpected error: \" + ce,ce));
        throw new InitializationException(LocalizableMessage.EMPTY,ce);
      }
    }
 else {
      println(installStatus.getInstallationMsg());
    }
  }
 else   if (installStatus.isInstalled()) {
    throw new InitializationException(installStatus.getInstallationMsg());
  }
}
```
Comment:
```
Checks if the server is installed or not.
```
---
id: 496

Code snippet:
```
public String format(DateTimeFormatter formatter){
  Objects.requireNonNull(formatter,\"formatter\");
  return formatter.format(this);
}
```
Comment:
```
Formats this time using the specified formatter. <p> this time will be passed to the formatter to produce a string.
```
---
id: 497

Code snippet:
```
private ResourceType(Builder builder){
  this.uuid=builder.uuid;
  this.name=builder.name;
  this.description=builder.description;
  this.patterns=Collections.unmodifiableSet(builder.patterns);
  this.actions=Collections.unmodifiableMap(builder.actions);
  this.createdBy=builder.createdBy;
  this.creationDate=builder.creationDate;
  this.lastModifiedBy=builder.lastModifiedBy;
  this.lastModifiedDate=builder.lastModifiedDate;
}
```
Comment:
```
Construct a resourcetype with the given builder.
```
---
id: 498

Code snippet:
```
public void handleButton1Request(RequestInvocationEvent event) throws ModelControlException {
  submitCycle=true;
  RMRealmModel model=(RMRealmModel)getModel();
  String realm=(String)getPageSessionAttribute(AMAdminConstants.CURRENT_REALM);
  AMPropertySheet ps=(AMPropertySheet)getChild(REALM_PROPERTIES);
  try {
    Map orig=model.getAttributeValues(realm);
    Map values=ps.getAttributeValues(orig,true,true,model);
    model.setAttributeValues(realm,values);
    setInlineAlertMessage(CCAlert.TYPE_INFO,\"message.information\",\"message.updated\");
  }
 catch (  AMConsoleException e) {
    setInlineAlertMessage(CCAlert.TYPE_ERROR,\"message.error\",e.getMessage());
  }
  forwardTo();
}
```
Comment:
```
Handles save button request.
```
---
id: 499

Code snippet:
```
public boolean computeScrollOffset(){
  if (isFinished()) {
    return false;
  }
switch (mMode) {
case SCROLL_MODE:
    long time=AnimationUtils.currentAnimationTimeMillis();
  final long elapsedTime=time - mScrollerX.mStartTime;
final int duration=mScrollerX.mDuration;
if (elapsedTime < duration) {
final float q=mInterpolator.getInterpolation(elapsedTime / (float)duration);
mScrollerX.updateScroll(q);
mScrollerY.updateScroll(q);
}
 else {
abortAnimation();
}
break;
case FLING_MODE:
if (!mScrollerX.mFinished) {
if (!mScrollerX.update()) {
if (!mScrollerX.continueWhenFinished()) {
mScrollerX.finish();
}
}
}
if (!mScrollerY.mFinished) {
if (!mScrollerY.update()) {
if (!mScrollerY.continueWhenFinished()) {
mScrollerY.finish();
}
}
}
break;
}
return true;
}
```
Comment:
```
Call this when you want to know the new location. if it returns true, the animation is not yet finished.
```
---
