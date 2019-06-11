id: 0

Code snippet:
```
@Override public void shutdown(){
  processServerShutdown(null);
  try {
    writer.flush();
    writer.close();
  }
 catch (  Exception e) {
    errorHandler.handleCloseError(e);
  }
}
```
Comment:
```
Shutdown the text writer.
```
---
id: 1

Code snippet:
```
public DERSequence(ASN1Encodable obj){
  super(obj);
}
```
Comment:
```
Create an object.
```
---
id: 2

Code snippet:
```
private boolean breakKeepAliveLoop(SocketWrapperBase<?> socketWrapper){
  openSocket=keepAlive;
  if (sendfileData != null && !getErrorState().isError()) {
    sendfileData.keepAlive=keepAlive;
switch (socketWrapper.processSendfile(sendfileData)) {
case DONE:
      sendfileData=null;
    return false;
case PENDING:
  return true;
case ERROR:
if (log.isDebugEnabled()) {
  log.debug(sm.getString(\"http11processor.sendfile.error\"));
}
setErrorState(ErrorState.CLOSE_CONNECTION_NOW,null);
return true;
}
}
return false;
}
```
Comment:
```
Checks to see if the keep-alive loop should be broken, performing any processing (e.g. sendfile handling) that may have an impact on whether or not the keep-alive loop should be broken.
```
---
id: 3

Code snippet:
```
public final TreeSet<BrdAbitPin> touching_pins_at_end_corners(){
  TreeSet<BrdAbitPin> result=new TreeSet<BrdAbitPin>();
  touching_pins_at_end_corners(result,corner_first());
  touching_pins_at_end_corners(result,corner_last());
  return result;
}
```
Comment:
```
Looks up touching pins at the first corner and the last corner of the trace. used to avoid acid traps.
```
---
id: 4

Code snippet:
```
public boolean isIs(){
  return is;
}
```
Comment:
```
Indicates if this attribute has an \"is\" getter.
```
---
id: 5

Code snippet:
```
public void logRequestInfo(HTTPRequestInfo requestInfo){
}
```
Comment:
```
Log a message.
```
---
id: 6

Code snippet:
```
@Override public int show(final FragmentTransaction transaction,final String tag){
  return delegate.show(transaction,tag);
}
```
Comment:
```
Show a message.
```
---
id: 7

Code snippet:
```
public static void registerBackendInitializationListener(BackendInitializationListener listener){
  directoryServer.backendInitializationListeners.add(listener);
}
```
Comment:
```
Registers the provided backend initialization listener with the directory server.
```
---
id: 8

Code snippet:
```
public void testAndNotPosPosFirstLonger(){
  byte aBytes[]={-128,9,56,100,-2,-76,89,45,91,3,-15,35,26,-117,23,87,-25,-75};
  byte bBytes[]={-2,-3,-4,-4,5,14,23,39,48,57,66,5,14,23};
  int aSign=1;
  int bSign=1;
  byte rBytes[]={0,-128,9,56,100,0,0,1,1,90,1,-32,0,10,-126,21,82,-31,-96};
  BigInteger aNumber=new BigInteger(aSign,aBytes);
  BigInteger bNumber=new BigInteger(bSign,bBytes);
  BigInteger result=aNumber.andNot(bNumber);
  byte resBytes[]=new byte[rBytes.length];
  resBytes=result.toByteArray();
  for (int i=0; i < resBytes.length; i++) {
    assertTrue(resBytes[i] == rBytes[i]);
  }
  assertEquals(\"incorrect sign\",1,result.signum());
}
```
Comment:
```
Add a positive numbers for a positive number.
```
---
id: 9

Code snippet:
```
public Point(Point p){
  this(p.x,p.y);
}
```
Comment:
```
Create a point.
```
---
id: 10

Code snippet:
```
private long calcChecksum(String filename) throws Exception {
  return calcChecksum(new File(filename));
}
```
Comment:
```
Calculates the size of the file.
```
---
id: 11

Code snippet:
```
@Override public void skippedEntity(String name) throws SAXException {
  if (saxLog.isDebugEnabled()) {
    saxLog.debug(\"skippedEntity(\" + name + \")\");
  }
}
```
Comment:
```
Receive notification of a notification.
```
---
id: 12

Code snippet:
```
public boolean isPrimaryServer(String serverID){
  return isSiteEnabled() ? getSiteID().equals(serverID) : localServerID.equals(serverID);
}
```
Comment:
```
Returns true if the connection is a valid connection.
```
---
id: 13

Code snippet:
```
protected boolean identityEquals(Identity identity){
  if (!name.equalsIgnoreCase(identity.name))   return false;
  if ((publicKey == null) ^ (identity.publicKey == null))   return false;
  if (publicKey != null && identity.publicKey != null)   if (!publicKey.equals(identity.publicKey))   return false;
  return true;
}
```
Comment:
```
Tests for equality between the specified identity and this identity. this method should be overriden by subclasses to test for equality. the default behavior is to return true if the names and public keys are equal.
```
---
id: 14

Code snippet:
```
public boolean isIgnoringCancelled(){
  return ignoreCancelled;
}
```
Comment:
```
Whether this listener accepts cancelled events.
```
---
id: 15

Code snippet:
```
public MapboxDirections(Builder builder){
  this.builder=builder;
}
```
Comment:
```
Mapbox builder.
```
---
id: 16

Code snippet:
```
public static String printHexBinary(byte[] val){
  if (theConverter == null)   initConverter();
  return theConverter.printHexBinary(val);
}
```
Comment:
```
<p> converts an array of bytes into a string.
```
---
id: 17

Code snippet:
```
public String encode(){
  return encode(new StringBuilder()).toString();
}
```
Comment:
```
Encode the address as a string and return it.
```
---
id: 18

Code snippet:
```
public void handleButton3Request(RequestInvocationEvent event){
  FSSAMLServiceViewBean vb=(FSSAMLServiceViewBean)getViewBean(FSSAMLServiceViewBean.class);
  backTrail();
  unlockPageTrailForSwapping();
  passPgSessionMap(vb);
  vb.setValues();
  vb.forwardTo(getRequestContext());
}
```
Comment:
```
Handles back button request.
```
---
id: 19

Code snippet:
```
public FilterServiceImpl(Context context){
  LOG.info(\"Creating AdguardService instance for {}\",context);
  this.context=context;
  filterListDao=new FilterListDaoImpl(context);
  filterRuleDao=new FilterRuleDaoImpl(context);
  preferencesService=ServiceLocator.getInstance(context).getPreferencesService();
}
```
Comment:
```
Construct a new instance.
```
---
id: 20

Code snippet:
```
public KeyNotFoundException(Throwable ex){
  super(ex);
}
```
Comment:
```
Creates a new keynotfoundexception datatype.
```
---
id: 21

Code snippet:
```
public String format(DateTimeFormatter formatter){
  Objects.requireNonNull(formatter,\"formatter\");
  return formatter.format(this);
}
```
Comment:
```
Formats the given date.
```
---
id: 22

Code snippet:
```
public UpgradeException(Throwable t){
  super(t);
}
```
Comment:
```
Constructs an <code>upgradeexception</code> with given <code>throwable</code>.
```
---
id: 23

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
id: 24

Code snippet:
```
public com.sun.identity.liberty.ws.common.jaxb.security.RequesterAuthorizationElement createRequesterAuthorizationElement() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.liberty.ws.common.jaxb.security.impl.RequesterAuthorizationElementImpl();
}
```
Comment:
```
Creates a <code>factory</code> object.
```
---
id: 25

Code snippet:
```
public static URI resolve(final URI baseURI,final String reference){
  return URIUtils.resolve(baseURI,URI.create(reference));
}
```
Comment:
```
Resolves a uri from the given uri.
```
---
id: 26

Code snippet:
```
public static void message(CommandManager mgr,String msg){
  dumpToOutput(mgr,msg,null);
  mgr.getDebugger().message(msg);
}
```
Comment:
```
Prints messages only when the debug state is either debug.message or debug.on. <p><b>note:</b> debugging is an io intensive operation and may hurt application performance when abused. particularly, note that java evaluates arguments to <code>message()</code> even when debugging is turned off. so when the argument to this method involves the string concatenation operator \'+\' or any other method invocation, <code>messageenabled</code> <b>must</b> be used. it is recommended that the debug state be checked by invoking <code>messageenabled()</code> before invoking any <code>message()</code> methods to avoid unnecessary argument evaluation and maximize application performance.</p>.
```
---
id: 27

Code snippet:
```
private static Object maskNull(Object key){
  return (key == null) ? NULL_KEY : key;
}
```
Comment:
```
Returns a map of the key from the specified key.
```
---
id: 28

Code snippet:
```
public static boolean isValidLifecycleCallback(Method method){
  if (method.getParameterTypes().length != 0 || Modifier.isStatic(method.getModifiers()) || method.getExceptionTypes().length > 0 || !method.getReturnType().getName().equals(\"void\")) {
    return false;
  }
  return true;
}
```
Comment:
```
Checks if the given object is a valid class.
```
---
id: 29

Code snippet:
```
public int position(){
  return pos;
}
```
Comment:
```
Returns this reader\'s position.
```
---
id: 30

Code snippet:
```
public DecisionImpl(String xml) throws XACMLException {
  Document document=XMLUtils.toDOMDocument(xml,XACMLSDKUtils.debug);
  if (document != null) {
    Element rootElement=document.getDocumentElement();
    processElement(rootElement);
    makeImmutable();
  }
 else {
    XACMLSDKUtils.debug.error(\"DecisionImpl.processElement(): invalid XML input\");
    throw new XACMLException(XACMLSDKUtils.xacmlResourceBundle.getString(\"errorObtainingElement\"));
  }
}
```
Comment:
```
Constructs a <code>decision</code> object from an xml string.
```
---
id: 31

Code snippet:
```
protected void ensureMyLastProtocolMessagesHaveRecords(List<ProtocolMessage> protocolMessages){
  for (int pmPointer=0; pmPointer < protocolMessages.size(); pmPointer++) {
    ProtocolMessage pm=protocolMessages.get(pmPointer);
    if (handlingMyLastProtocolMessageWithContentType(protocolMessages,pmPointer)) {
      if (pm.getRecords() == null || pm.getRecords().isEmpty()) {
        pm.addRecord(new Record());
      }
    }
  }
}
```
Comment:
```
Every last protocol message that is going to be sent from my peer has to have a record.
```
---
id: 32

Code snippet:
```
public void startPrefixMapping(String prefix,String uri){
}
```
Comment:
```
Adapt a sax2 start prefix mapping event.
```
---
id: 33

Code snippet:
```
private PrivilegeUtils(){
}
```
Comment:
```
Constructs xacmlprivilegeutils.
```
---
id: 34

Code snippet:
```
public static Fragment1 newInstance(int sectionNumber){
  Fragment1 fragment=new Fragment1();
  Bundle args=new Bundle();
  args.putInt(ARG_SECTION_NUMBER,sectionNumber);
  fragment.setArguments(args);
  return fragment;
}
```
Comment:
```
Returns a new instance of this fragment for the given section number.
```
---
id: 35

Code snippet:
```
public static void fill(char[] array,int start,int end,char value){
  Arrays.checkStartAndEnd(array.length,start,end);
  for (int i=start; i < end; i++) {
    array[i]=value;
  }
}
```
Comment:
```
Fills the specified range in the array with the specified element.
```
---
id: 36

Code snippet:
```
public void visitLineNumber(int line,Label start){
  if (mv != null) {
    mv.visitLineNumber(line,start);
  }
}
```
Comment:
```
Visits an instruction.
```
---
id: 37

Code snippet:
```
public CompositeContext createContext(ColorModel srcColorModel,ColorModel dstColorModel,RenderingHints hints){
  return new SunCompositeContext(this,srcColorModel,dstColorModel);
}
```
Comment:
```
Creates a <code>null</code> with the specified parameters.
```
---
id: 38

Code snippet:
```
public boolean isBearer(){
  if (_statements == null || _statements.isEmpty()) {
    return false;
  }
  Iterator iter=_statements.iterator();
  while (iter.hasNext()) {
    Object statement=iter.next();
    if (!(statement instanceof SubjectStatement)) {
      continue;
    }
    Subject subject=((SubjectStatement)statement).getSubject();
    if (subject == null) {
      continue;
    }
    SubjectConfirmation sc=subject.getSubjectConfirmation();
    if (sc == null) {
      continue;
    }
    Set confirmationMethods=sc.getConfirmationMethod();
    if (confirmationMethods == null || confirmationMethods.isEmpty()) {
      continue;
    }
    if (confirmationMethods.contains(SAMLConstants.CONFIRMATION_METHOD_BEARER)) {
      return true;
    }
  }
  return false;
}
```
Comment:
```
Determines if the <code>securityassertion</code> contains saml bearer confirmation method.
```
---
id: 39

Code snippet:
```
public ExpectedImpl(T value){
  this.value=Objects.requireNonNull(value);
}
```
Comment:
```
Creates a new instance.
```
---
id: 40

Code snippet:
```
@Override protected void finalize(){
  disconnect(DisconnectReason.OTHER,false,null);
}
```
Comment:
```
Cleans up the connection.
```
---
id: 41

Code snippet:
```
public HomesUserDatabase(){
  super();
}
```
Comment:
```
Creates a new instance.
```
---
id: 42

Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  NodeList elementList;
  Node testAddress;
  NamedNodeMap attributes;
  Node removedNode;
  String value;
  doc=(Document)load(\"staff\",true);
  elementList=doc.getElementsByTagName(\"address\");
  testAddress=elementList.item(2);
  attributes=testAddress.getAttributes();
  removedNode=attributes.removeNamedItem(\"street\");
  value=removedNode.getNodeValue();
  assertEquals(\"namednodemapRemoveNamedItemReturnNodeValueAssert\",\"No\",value);
}
```
Comment:
```
Runs the test case.
```
---
id: 43

Code snippet:
```
public StateAttribute(byte[] octets){
  super(octets);
  state=new String(octets,2,octets.length - 2,Charset.forName(\"utf-8\"));
}
```
Comment:
```
Creates a replymessageattribute from the on-the-wire octets.
```
---
id: 44

Code snippet:
```
@BeforeClass public void startServer() throws Exception {
  TestCaseUtils.startServer();
}
```
Comment:
```
Ensures that the directory server is running.
```
---
id: 45

Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(characterdatareplacedatamiddle.class,args);
}
```
Comment:
```
Runs this test from the command line.
```
---
id: 46

Code snippet:
```
public void stopReplicationServers(Collection<HostPort> serversToDisconnect){
  for (  ReplicationServerHandler rsHandler : connectedRSs.values()) {
    if (serversToDisconnect.contains(HostPort.valueOf(rsHandler.getServerAddressURL()))) {
      stopServer(rsHandler,false);
    }
  }
}
```
Comment:
```
Stop the server.
```
---
id: 47

Code snippet:
```
public void stopStreaming(){
synchronized (SyncOp) {
    videoClient.stopStreaming();
    audioClient.stop();
    rtmpSender.stop();
    LogTools.d(\"RESClient,stopStreaming()\");
  }
}
```
Comment:
```
Stop streaming.
```
---
id: 48

Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(documentimportnode12.class,args);
}
```
Comment:
```
Runs this test from the command line.
```
---
id: 49

Code snippet:
```
public void logException(Throwable ex){
  if (needsLogging) {
    this.getLogger().error(ex.getMessage(),ex);
  }
}
```
Comment:
```
Log an exception.
```
---
id: 50

Code snippet:
```
public void put(E e){
  offer(e);
}
```
Comment:
```
Adds a new element to the queue.
```
---
id: 51

Code snippet:
```
@Override public boolean isPrintValue(Object bean,Object bean2,String attrName,StoreDescription desc){
  boolean isPrint=super.isPrintValue(bean,bean2,attrName,desc);
  if (isPrint) {
    if (\"jkHome\".equals(attrName)) {
      Connector connector=((Connector)bean);
      File catalinaBase=getCatalinaBase();
      File jkHomeBase=getJkHomeBase((String)connector.getProperty(\"jkHome\"),catalinaBase);
      isPrint=!catalinaBase.equals(jkHomeBase);
    }
  }
  return isPrint;
}
```
Comment:
```
<p>checks if the given <code>object</code> is <code>null</code> or <code>null</code>.
```
---
id: 52

Code snippet:
```
private boolean isAllowedByIp(String ip) throws PolicyException {
  boolean allowed=false;
  long requestIp=stringToIp(ip);
  Iterator ipValues=ipList.iterator();
  while (ipValues.hasNext()) {
    long startIp=((Long)ipValues.next()).longValue();
    if (ipValues.hasNext()) {
      long endIp=((Long)ipValues.next()).longValue();
      if ((requestIp >= startIp) && (requestIp <= endIp)) {
        allowed=true;
        break;
      }
    }
  }
  if ((requestIp >= startIp) && (requestIp <= endIp)) {
    allowed=true;
  }
  return allowed;
}
```
Comment:
```
Checks of the ip falls in the valid range between start and end ip adrresses.
```
---
id: 53

Code snippet:
```
private boolean contains(String[] names,String name){
  assert name != null;
  for (int i=0; i < names.length; i++) {
    if (name.equals(names[i])) {
      return true;
    }
  }
  return false;
}
```
Comment:
```
Returns true if the given name is a name.
```
---
id: 54

Code snippet:
```
public void testCase1(){
  byte aBytes[]={1,2,3,4,5,6,7};
  byte bBytes[]={0};
  int aSign=1;
  int bSign=0;
  BigInteger aNumber=new BigInteger(aSign,aBytes);
  BigInteger bNumber=new BigInteger(bSign,bBytes);
  try {
    aNumber.divide(bNumber);
    fail(\"ArithmeticException has not been caught\");
  }
 catch (  ArithmeticException e) {
  }
}
```
Comment:
```
Divide by zero.
```
---
id: 55

Code snippet:
```
public void unsetCompression(){
  if (getCompressionMode() != MODE_EXPLICIT) {
    throw new IllegalStateException(\"Compression mode not MODE_EXPLICIT!\");
  }
  this.compressionQuality=JPEG.DEFAULT_QUALITY;
}
```
Comment:
```
Removes any previous compression quality setting. <p> the default implementation resets the compression quality to <code>0.75f</code>.
```
---
id: 56

Code snippet:
```
public GenericPrincipal(String name,String password,List<String> roles,Principal userPrincipal,LoginContext loginContext,GSSCredential gssCredential){
  super();
  this.name=name;
  this.password=password;
  this.userPrincipal=userPrincipal;
  if (roles == null) {
    this.roles=new String[0];
  }
 else {
    this.roles=roles.toArray(new String[roles.size()]);
    if (this.roles.length > 1) {
      Arrays.sort(this.roles);
    }
  }
  this.loginContext=loginContext;
  this.gssCredential=gssCredential;
}
```
Comment:
```
Construct a new principal, associated with the specified realm, for the specified username and password, with the specified role names (as strings).
```
---
id: 57

Code snippet:
```
static void writeStringToFile(final String string,final File file) throws IOException {
  createFile(file);
  try (PrintWriter printWriter=new PrintWriter(file)){
    printWriter.print(string);
  }
 }
```
Comment:
```
Write a file to a file.
```
---
id: 58

Code snippet:
```
private void addDataAndRegisteredParamId(Long ruleActionId,Event event,HashMap<Long,String> paramsData,HashMap<Long,Long> paramsRegisteredParamId){
  if (!database.isOpen()) {
    throw new IllegalStateException(TAG + \" is already closed.\");
  }
  Long paramId;
  String paramData;
  Long paramRegisteredParamId;
  Cursor cursor=ruleActionParameterDbAdapter.fetchAll(ruleActionId,null,null);
  for (int i=0; i < cursor.getCount(); i++) {
    cursor.moveToNext();
    paramId=getLongFromCursor(cursor,RuleActionParameterDbAdapter.KEY_RULEACTIONPARAMETERID);
    paramData=getStringFromCursor(cursor,RuleActionParameterDbAdapter.KEY_RULEACTIONPARAMETERDATA);
    paramRegisteredParamId=getLongFromCursor(cursor,RuleActionParameterDbAdapter.KEY_ACTIONPARAMETERID);
    paramsData.put(paramId,fillParamWithEventAttrib(paramData,event));
    paramsRegisteredParamId.put(paramId,paramRegisteredParamId);
  }
  cursor.close();
}
```
Comment:
```
Adds a request to the database.
```
---
id: 59

Code snippet:
```
private void deleteSubtree(DN dn) throws LdapException {
  for (  DN child : listEntries(dn,Filter.objectClassPresent())) {
    deleteSubtree(child);
  }
  connection.delete(dn.toString());
}
```
Comment:
```
Delete a node.
```
---
id: 60

Code snippet:
```
public void readByteArray(byte[] arr,int offset) throws InvalidDataTypeException {
  if (arr == null) {
    throw new NullPointerException(\"Byte array is null\");
  }
  if ((offset < 0) || (offset >= arr.length)) {
    throw new InvalidDataTypeException(\"Offset to byte array is out of bounds: offset = \" + offset + \", array.length = \"+ arr.length);
  }
  if (offset + size > arr.length) {
    throw new InvalidDataTypeException(\"Offset plus size to byte array is out of bounds: offset = \" + offset + \", size = \"+ size+ \" + arr.length \"+ arr.length);
  }
  long lvalue=0;
  for (int i=offset; i < (offset + size); i++) {
    lvalue<<=8;
    lvalue+=(arr[i] & 0xff);
  }
  value=lvalue;
  logger.config(\"Read NumberFixedlength:\" + value);
}
```
Comment:
```
Reads an array of bytes from a byte array.
```
---
id: 61

Code snippet:
```
private void removeMatchingRuleUse(String definition,SchemaBuilder newSchemaBuilder,Set<String> modifiedSchemaFiles) throws DirectoryException {
  Schema currentSchema=newSchemaBuilder.toSchema();
  String mruOid=SchemaUtils.parseMatchingRuleUseOID(definition);
  if (!currentSchema.hasMatchingRuleUse(mruOid)) {
    LocalizableMessage message=ERR_SCHEMA_MODIFY_REMOVE_NO_SUCH_MR_USE.get(mruOid);
    throw new DirectoryException(ResultCode.UNWILLING_TO_PERFORM,message);
  }
  newSchemaBuilder.removeMatchingRuleUse(mruOid);
  addElementIfNotNull(modifiedSchemaFiles,getElementSchemaFile(currentSchema.getMatchingRuleUse(mruOid)));
}
```
Comment:
```
Handles all processing required to remove the provided matching rule use from the server schema, ensuring all other metadata is properly updated. note that this method will first check to see whether the same matching rule use will be later added to the server schema with an updated definition, and if so then the removal will be ignored because the later add will be handled as a replace. if the matching rule use will not be replaced with a new definition, then this method will ensure that there are no other schema elements that depend on the matching rule use before allowing it to be removed.
```
---
id: 62

Code snippet:
```
public static String removeSlashFromEnd(String string){
  if (string != null && !string.equals(\"\") && string.charAt(string.length() - 1) == \'/\') {
    return string.substring(0,string.length() - 1);
  }
  return string;
}
```
Comment:
```
Removes a string from a string.
```
---
id: 63

Code snippet:
```
private void handlePrivilegeUpdates() throws SSOException, SMSException {
  for (  ChangeSet<String,Set<String>> change : privilegeUpdates) {
    final String configName=change.getIdentifier();
    final Set<String> newPermissions=change.getData();
    final ServiceConfig privilegeConfig=privilegesConfig.getSubConfig(configName);
    privilegeConfig.addAttribute(LIST_OF_PERMISSIONS,newPermissions);
  }
}
```
Comment:
```
This method is called when the application has changed.
```
---
id: 64

Code snippet:
```
public void testCase6(){
  byte aBytes[]={1,2,3,4,5,6,7,1,2,3};
  byte bBytes[]={10,20,30,40,50,60,70,10,20,30};
  int aSign=-1;
  int bSign=-1;
  byte rBytes[]={9,18,27,36,45,54,63,9,18,27};
  BigInteger aNumber=new BigInteger(aSign,aBytes);
  BigInteger bNumber=new BigInteger(bSign,bBytes);
  BigInteger result=aNumber.subtract(bNumber);
  byte resBytes[]=new byte[rBytes.length];
  resBytes=result.toByteArray();
  for (int i=0; i < resBytes.length; i++) {
    assertTrue(resBytes[i] == rBytes[i]);
  }
  assertEquals(1,result.signum());
}
```
Comment:
```
Add two positive numbers.
```
---
id: 65

Code snippet:
```
public void update(Graphics a,JComponent b){
  for (int i=0; i < uis.size(); i++) {
    ((ComponentUI)(uis.elementAt(i))).update(a,b);
  }
}
```
Comment:
```
Invokes the <code>paint</code> method on the ui thread.
```
---
id: 66

Code snippet:
```
public synchronized void close() throws IOException {
  isClosed=true;
  localAddress=Inet4Address.ANY;
  impl.close();
}
```
Comment:
```
Closes the socket. it is not possible to reconnect or rebind to this socket thereafter which means a new socket instance has to be created.
```
---
id: 67

Code snippet:
```
@Override public void lifecycleEvent(LifecycleEvent event){
  try {
    host=(Host)event.getLifecycle();
    if (host instanceof StandardHost) {
      setCopyXML(((StandardHost)host).isCopyXML());
      setDeployXML(((StandardHost)host).isDeployXML());
      setUnpackWARs(((StandardHost)host).isUnpackWARs());
      setContextClass(((StandardHost)host).getContextClass());
    }
  }
 catch (  ClassCastException e) {
    log.error(sm.getString(\"hostConfig.cce\",event.getLifecycle()),e);
    return;
  }
  if (event.getType().equals(Lifecycle.PERIODIC_EVENT)) {
    check();
  }
 else   if (event.getType().equals(Lifecycle.BEFORE_START_EVENT)) {
    beforeStart();
  }
 else   if (event.getType().equals(Lifecycle.START_EVENT)) {
    start();
  }
 else   if (event.getType().equals(Lifecycle.STOP_EVENT)) {
    stop();
  }
}
```
Comment:
```
Process the start event for an associated host.
```
---
id: 68

Code snippet:
```
public void removeTreeModelListener(TreeModelListener l){
  listenerList.remove(TreeModelListener.class,l);
}
```
Comment:
```
Removes a listener.
```
---
id: 69

Code snippet:
```
public static int dehexchar(char hex){
  if (hex >= \'0\' && hex <= \'9\') {
    return hex - \'0\';
  }
 else   if (hex >= \'A\' && hex <= \'F\') {
    return hex - \'A\' + 10;
  }
 else   if (hex >= \'a\' && hex <= \'f\') {
    return hex - \'a\' + 10;
  }
 else {
    return -1;
  }
}
```
Comment:
```
Converts a byte array to a string.
```
---
id: 70

Code snippet:
```
public SQLIntegrityConstraintViolationException(String reason,Throwable cause){
  super(reason,cause);
}
```
Comment:
```
Creates a new <code>sqlexception</code> with the specified detail message.
```
---
id: 71

Code snippet:
```
private void assertUniqueMod(List<Modification> mods,ModificationType modType,String value){
  assertThat(mods).hasSize(1);
  Modification mod=mods.get(0);
  assertEquals(mod.getModificationType(),modType);
  String firstVal=mod.getAttribute().iterator().next().toString();
  assertEquals(firstVal,value);
}
```
Comment:
```
Check that the mods given as first parameter match the next parameters.
```
---
id: 72

Code snippet:
```
public int doRead(ByteChunk chunk) throws IOException {
  int n=inputBuffer.doRead(chunk);
  if (n > 0) {
    bytesRead+=n;
  }
  return n;
}
```
Comment:
```
Flushes the contents of the stream.
```
---
id: 73

Code snippet:
```
public static boolean isExpired(){
  return getInstance().expired;
}
```
Comment:
```
Returns true if this message is not enabled.
```
---
id: 74

Code snippet:
```
ForkJoinWorkerThread(ForkJoinPool pool,ThreadGroup threadGroup,AccessControlContext acc){
  super(threadGroup,null,\"aForkJoinWorkerThread\");
  U.putOrderedObject(this,INHERITEDACCESSCONTROLCONTEXT,acc);
  eraseThreadLocals();
  this.pool=pool;
  this.workQueue=pool.registerWorker(this);
}
```
Comment:
```
Creates a new instance.
```
---
id: 75

Code snippet:
```
void attachView(){
  getPresenter().attachView(delegateCallback.getMvpView());
}
```
Comment:
```
Attaches the view to the presenter.
```
---
id: 76

Code snippet:
```
public static boolean matchSecret(String secret){
  return secretSet.remove(secret);
}
```
Comment:
```
Checks whether the given key is a valid password.
```
---
id: 77

Code snippet:
```
public static boolean skip_scope(JflexScanner p_scanner){
  int open_bracked_count=1;
  while (open_bracked_count > 0) {
    p_scanner.yybegin(DsnFileScanner.NAME);
    Object curr_token=null;
    try {
      curr_token=p_scanner.next_token();
    }
 catch (    Exception e) {
      System.err.println(\"ScopeKeyword.skip_scope: Error while scanning file\");
      System.err.println(e);
      return false;
    }
    if (curr_token == null) {
      return false;
    }
    if (curr_token == DsnKeyword.OPEN_BRACKET) {
      ++open_bracked_count;
    }
 else     if (curr_token == DsnKeyword.CLOSED_BRACKET) {
      --open_bracked_count;
    }
  }
  return true;
}
```
Comment:
```
Attempts to parse a string.
```
---
id: 78

Code snippet:
```
public GSSAPISASLMechanismHandler(){
  super();
}
```
Comment:
```
Creates a new instance of this sasl mechanism handler. no initialization should be done in this method, as it should all be performed in the <code>initializesaslmechanismhandler</code> method.
```
---
id: 79

Code snippet:
```
private int normalizePort(int port,String host){
  if ((1 <= port && port <= 65535) || (port == 0 && host == null)) {
    return port;
  }
  throw new IllegalArgumentException(\"Invalid network port provided: \" + port + \" is not included in the [1, 65535] range.\");
}
```
Comment:
```
Ensures the supplied port number is valid.
```
---
id: 80

Code snippet:
```
public ProgressMonitor(Component parentComponent,Object message,String note,int min,int max){
  this(parentComponent,message,note,min,max,null);
}
```
Comment:
```
Creates a new <code>action</code>.
```
---
id: 81

Code snippet:
```
private Node addConditionWaiter(){
  Node t=lastWaiter;
  if (t != null && t.waitStatus != Node.CONDITION) {
    unlinkCancelledWaiters();
    t=lastWaiter;
  }
  Node node=new Node(Thread.currentThread(),Node.CONDITION);
  if (t == null)   firstWaiter=node;
 else   t.nextWaiter=node;
  lastWaiter=node;
  return node;
}
```
Comment:
```
Adds a new waiter to wait queue.
```
---
id: 82

Code snippet:
```
private Object writeReplace(){
  return new Ser(Ser.ZOT,this);
}
```
Comment:
```
Writes the object using a <a href=\"../../../serialized-form.html#java.time.zone.ser\">dedicated serialized form</a>.
```
---
id: 83

Code snippet:
```
public static void print(Object... params){
  String fullText=buildToString(params);
  System.out.println(fullText);
}
```
Comment:
```
Prints a string.
```
---
id: 84

Code snippet:
```
public static Component createHorizontalGlue(){
  return new Filler(new Dimension(0,0),new Dimension(0,0),new Dimension(Short.MAX_VALUE,0));
}
```
Comment:
```
Creates a horizontal glue component.
```
---
id: 85

Code snippet:
```
static void testFailLoadAndGc() throws TestFailed {
  try {
    BrokenDexLoader loader;
    loader=new BrokenDexLoader(ClassLoader.getSystemClassLoader());
    loader.findBrokenClass();
    System.err.println(\"ERROR: Inaccessible was accessible\");
  }
 catch (  InvocationTargetException ite) {
    Throwable cause=ite.getCause();
    if (cause instanceof NullPointerException) {
      System.err.println(\"Got expected ITE/NPE\");
    }
 else {
      System.err.println(\"Got unexpected ITE\");
      ite.printStackTrace();
    }
  }
}
```
Comment:
```
Tests that the class can be loaded.
```
---
id: 86

Code snippet:
```
public JTabbedPane(int tabPlacement,int tabLayoutPolicy){
  setTabPlacement(tabPlacement);
  setTabLayoutPolicy(tabLayoutPolicy);
  pages=new ArrayList<Page>(1);
  setModel(new DefaultSingleSelectionModel());
  updateUI();
}
```
Comment:
```
Creates a new instance.
```
---
id: 87

Code snippet:
```
public void onCreate(Bundle savedInstanceState){
  Session session=Session.getActiveSession();
  if (session == null) {
    if (savedInstanceState != null) {
      session=Session.restoreSession(activity,null,callback,savedInstanceState);
    }
    if (session == null) {
      session=new Session(activity);
    }
    Session.setActiveSession(session);
  }
  if (savedInstanceState != null) {
    String callIdString=savedInstanceState.getString(DIALOG_CALL_ID_SAVE_KEY);
    if (callIdString != null) {
      pendingFacebookDialogCallId=UUID.fromString(callIdString);
    }
    pendingFacebookDialogCallStore.restoreFromSavedInstanceState(savedInstanceState);
  }
}
```
Comment:
```
To be called from an activity or fragment\'s oncreate method.
```
---
id: 88

Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(attreffectivevalue.class,args);
}
```
Comment:
```
Runs this test from the command line.
```
---
id: 89

Code snippet:
```
public static ComponentUI createUI(JComponent c){
  throw new Error(\"ComponentUI.createUI not implemented.\");
}
```
Comment:
```
Creates a new instance.
```
---
id: 90

Code snippet:
```
public XMLElement newElementFromXMLFragment(String xmlFragment) throws Exception {
  StringReader reader=new StringReader(xmlFragment);
  ArrayList newTokens=getParser().parse(reader);
  ArrayList filteredTokens=getFilteredTokens(newTokens);
  ArrayList elements=getElements(filteredTokens);
  if (elements == null || elements.size() != 1) {
    throw new Exception(\"Failed to parse fragment into new element\");
  }
  return (XMLElement)elements.get(0);
}
```
Comment:
```
A factory method used for the creation of new xml elements that can be added to this xml document at a later stage. when this method is called, a new <code>xmlelement</code> object is returned to the caller. however, this newly created element is still not attached to the document anywhere and it is the responsiblity of the caller to attach it in the appropriate location. note that the supplied parameter <code>xmlfragement</code> must be a valid well-formed xml element.
```
---
id: 91

Code snippet:
```
public static String dateToString(final Date date){
  return dateToString(date,UTC_DATE_FORMAT,UTC_TIME_ZONE);
}
```
Comment:
```
Convert a date to a string.
```
---
id: 92

Code snippet:
```
public void removeQualifiers(){
  PropertyOptions opts=getOptions();
  opts.setHasQualifiers(false);
  opts.setHasLanguage(false);
  opts.setHasType(false);
  qualifier=null;
}
```
Comment:
```
Removes the given instance.
```
---
id: 93

Code snippet:
```
public final void addAttribute(String uri,String local,String qname,String type,String val){
  int index=super.getLength();
  super.addAttribute(uri,local,qname,type,val);
  if (index < MAXMinus1) {
    return;
  }
 else   if (index == MAXMinus1) {
    switchOverToHash(MAX);
  }
 else {
    Integer i=new Integer(index);
    m_indexFromQName.put(qname,i);
    m_buff.setLength(0);
    m_buff.append(\'{\').append(uri).append(\'}\').append(local);
    String key=m_buff.toString();
    m_indexFromQName.put(key,i);
  }
  return;
}
```
Comment:
```
This method adds the attribute, but also records its qname/index pair in the hashtable for fast lookup by getindex(qname).
```
---
id: 94

Code snippet:
```
public void invokeAndWait(Runnable task){
  if (roomLock.isHeldByCurrentThread()) {
    if (cachedRunnables == null) {
      cachedRunnables=new ArrayList<>();
    }
    cachedRunnables.add(task);
  }
 else {
    roomLock.lock();
    try {
      cachedRunnables=null;
      if (!closed) {
        task.run();
      }
      if (cachedRunnables != null) {
        for (int i=0; i < cachedRunnables.size(); i++) {
          if (!closed) {
            cachedRunnables.get(i).run();
          }
        }
        cachedRunnables=null;
      }
    }
  finally {
      roomLock.unlock();
    }
  }
}
```
Comment:
```
Submits the given runnable to the room executor and waits until it has been executed. currently, this simply means that the runnable will be run directly inside of a synchronized() block.<br> note that if a runnable recursively calls invokeandwait() with another runnable on this room, it will not be executed recursively, but instead cached until the original runnable is finished, to keep the behavior of using a executor.
```
---
id: 95

Code snippet:
```
public JobService jobRangeByType(String type,String state,long from,long to,String order,Handler<AsyncResult<List<Job>>> handler){
  delegate.jobRangeByType(type,state,from,to,order,handler);
  return this;
}
```
Comment:
```
Creates a new instance.
```
---
id: 96

Code snippet:
```
static void putFederation(String realm,String federationId,FederationElement federation){
  String cacheKey=buildCacheKey(realm,federationId);
  if (federation != null) {
    if (debug.messageEnabled()) {
      debug.message(\"WSFederationMetaCache.putFederation: \" + \"cacheKey = \" + cacheKey);
    }
    federationCache.put(cacheKey,federation);
  }
 else {
    if (debug.messageEnabled()) {
      debug.message(\"WSFederationMetaCache.putFederation: delete cacheEey = \" + cacheKey);
    }
    federationCache.remove(cacheKey);
    configCache.remove(cacheKey);
  }
}
```
Comment:
```
Puts the specified key into the cache.
```
---
id: 97

Code snippet:
```
@Override public String toString(){
  String s=null;
  try {
    s=toJSONObject().toString(2);
  }
 catch (  JSONException e) {
    PrivilegeManager.debug.error(\"EntitlementSubjectImpl.toString\",e);
  }
  return s;
}
```
Comment:
```
Returns string representation of the object.
```
---
id: 98

Code snippet:
```
private void hideBothNavigationBarAndStatusBar(){
  View decorView=getWindow().getDecorView();
  if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.JELLY_BEAN) {
    int uiOptions=View.SYSTEM_UI_FLAG_HIDE_NAVIGATION | View.SYSTEM_UI_FLAG_FULLSCREEN;
    decorView.setSystemUiVisibility(uiOptions);
  }
}
```
Comment:
```
// hide both the navigation bar and the status bar. // system_ui_flag_fullscreen is only available on android 4.1 and higher, but as // a general rule, you should design your app to hide the status bar whenever you // hide the navigation bar.
```
---
id: 99

Code snippet:
```
public boolean ready() throws IOException {
synchronized (lock) {
    ensureOpen();
    return true;
  }
}
```
Comment:
```
Tells whether this stream is ready to be read.
```
---
