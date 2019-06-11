id: 0

Code snippet:
```
public int intValue(){
  return intValue;
}
```
Comment:
```
Returns the integer value of this alias dereferencing policy as defined in rfc 4511 section 4.5.1.
```
---
id: 1

Code snippet:
```
@Override public void end(String namespace,String name) throws Exception {
  Object top=digester.pop();
  if (digester.log.isDebugEnabled()) {
    digester.log.debug(\"[ObjectCreateRule]{\" + digester.match + \"} Pop \"+ top.getClass().getName());
  }
}
```
Comment:
```
Description of the method.
```
---
id: 2

Code snippet:
```
protected void handleSESSION_EXPIRED(SessionMessage msg,Member sender) throws IOException {
  counterReceive_EVT_SESSION_EXPIRED++;
  DeltaSession session=(DeltaSession)findSession(msg.getSessionID());
  if (session != null) {
    if (log.isDebugEnabled()) {
      log.debug(sm.getString(\"deltaManager.receiveMessage.expired\",getName(),msg.getSessionID()));
    }
    session.expire(notifySessionListenersOnReplication,false);
  }
}
```
Comment:
```
Handle receive session is expire at other node ( expire session also here).
```
---
id: 3

Code snippet:
```
public boolean isEmpty(){
  return this.content.length == 0;
}
```
Comment:
```
This method checks if the binary data is empty. <br> disregarding the type of the descriptor its content is stored as a byte array.
```
---
id: 4

Code snippet:
```
public AsfTag(final Tag source,final boolean copy) throws UnsupportedEncodingException {
  this(copy);
  copyFrom(source);
}
```
Comment:
```
Creates an instance and copies the fields of the source into the own structure.<br>.
```
---
id: 5

Code snippet:
```
protected OrientationRequested(int value){
  super(value);
}
```
Comment:
```
Creates a new <code>drminforest</code> instance.
```
---
id: 6

Code snippet:
```
public synchronized void enableAttribute(String name) throws java.lang.IllegalArgumentException {
  if (name == null) {
    throw new java.lang.IllegalArgumentException(\"The name cannot be null.\");
  }
  if (!enabledAttributes.contains(name)) {
    enabledAttributes.addElement(name);
  }
}
```
Comment:
```
Enables all the attribute change notifications the attribute name of which equals the specified name to be sent to the listener. <br>if the specified name is already in the list of enabled attribute names, this method has no effect.
```
---
id: 7

Code snippet:
```
public Map<String,Set<String>> evaluate(Subject adminSubject,String realm,Subject subject,String resourceName,Map<String,Set<String>> environment) throws EntitlementException {
  Map<String,Set<String>> map=new HashMap<String,Set<String>>();
  map.put(propertyName,propertyValues);
  return map;
}
```
Comment:
```
Returns resoruce attributes aplicable to the request.
```
---
id: 8

Code snippet:
```
public ListItem(){
  super();
  role=PdfName.LBody;
}
```
Comment:
```
Creates a listitem.
```
---
id: 9

Code snippet:
```
public Role(String roleName,List<ObjectName> roleValue) throws IllegalArgumentException {
  if (roleName == null || roleValue == null) {
    String excMsg=\"Invalid parameter\";
    throw new IllegalArgumentException(excMsg);
  }
  setRoleName(roleName);
  setRoleValue(roleValue);
  return;
}
```
Comment:
```
Gets the role of the specified role.
```
---
id: 10

Code snippet:
```
public void paintTableBackground(SynthContext context,Graphics g,int x,int y,int w,int h){
  paintBackground(context,g,x,y,w,h,null);
}
```
Comment:
```
Paints the background of a table.
```
---
id: 11

Code snippet:
```
private String htmlDecode(String content){
  return Jsoup.parse(content).text();
}
```
Comment:
```
Sets the content.
```
---
id: 12

Code snippet:
```
protected void removeFromClientMap(String ct,Client c){
  clientTypeMap.remove(ct);
  mergedClientData.remove(ct);
  String ua=null;
  if ((c != null) && ((ua=c.getProperty(USER_AGENT)) != null)) {
    userAgentMap.remove(ua);
  }
  removeFromProfilesMap(ct,c);
}
```
Comment:
```
Complements addtoclientmap().
```
---
id: 13

Code snippet:
```
private CommonArguments(){
}
```
Comment:
```
Constructs a new exception with <code>null</code> as its detail message. the cause is not initialized.
```
---
id: 14

Code snippet:
```
public SecurityException(String message,Throwable cause){
  super(message,cause);
}
```
Comment:
```
Constructs a new exception with the specified detail message, cause, and bean for jax-ws exception serialization.
```
---
id: 15

Code snippet:
```
public Builder rootCa(Certificate rootCa){
  this.rootCa=rootCa;
  return this;
}
```
Comment:
```
A root ca to include in the final store.
```
---
id: 16

Code snippet:
```
static void writeArrayTable(ObjectOutputStream s,ArrayTable table) throws IOException {
  Object keys[];
  if (table == null || (keys=table.getKeys(null)) == null) {
    s.writeInt(0);
  }
 else {
    int validCount=0;
    for (int counter=0; counter < keys.length; counter++) {
      Object key=keys[counter];
      if ((key instanceof Serializable && table.get(key) instanceof Serializable) || (key instanceof ClientPropertyKey && ((ClientPropertyKey)key).getReportValueNotSerializable())) {
        validCount++;
      }
 else {
        keys[counter]=null;
      }
    }
    s.writeInt(validCount);
    if (validCount > 0) {
      for (      Object key : keys) {
        if (key != null) {
          s.writeObject(key);
          s.writeObject(table.get(key));
          if (--validCount == 0) {
            break;
          }
        }
      }
    }
  }
}
```
Comment:
```
Writes the passed in arraytable to the passed in objectoutputstream. the data is saved as an integer indicating how many key/value pairs are being archived, followed by the the key/value pairs. if <code>table</code> is null, 0 will be written to <code>s</code>. <p> this is a convenience method that actionmap/inputmap and abstractaction use to avoid having the same code in each class.
```
---
id: 17

Code snippet:
```
public static long longForQuery(SQLiteDatabase db,String query,String[] selectionArgs){
  SQLiteStatement prog=db.compileStatement(query);
  try {
    return longForQuery(prog,selectionArgs);
  }
  finally {
    prog.close();
  }
}
```
Comment:
```
Utility method to run the query on the db and return the value in the first column of the first row.
```
---
id: 18

Code snippet:
```
public boolean userHasReadAdminPrivs(SSOToken token,String realm) throws DelegationException, SSOException {
  DelegationPermission dp=delegationPermissionFactory.newInstance(realm,\"rest\",\"1.0\",\"sessions\",\"getProperty\",Collections.singleton(\"READ\"),Collections.<String,String>emptyMap());
  return delegationEvaluator.isAllowed(token,dp,Collections.<String,Set<String>>emptyMap());
}
```
Comment:
```
Returns true if the user is an administrator, or if it has delegated permissions to perform this request.
```
---
id: 19

Code snippet:
```
public com.sun.identity.wsfederation.jaxb.xmlsig.KeyNameElement createKeyNameElement(java.lang.String value) throws javax.xml.bind.JAXBException {
  return new com.sun.identity.wsfederation.jaxb.xmlsig.impl.KeyNameElementImpl(value);
}
```
Comment:
```
Create an instance of keynameelement.
```
---
id: 20

Code snippet:
```
public void columnRemoved(TableColumnModelEvent e){
  resizeAndRepaint();
}
```
Comment:
```
Overridden for performance reasons. see the <a href=\"#override\">implementation note</a> for more information.
```
---
id: 21

Code snippet:
```
public SendNotificationException(Throwable t){
  super(t.getMessage());
}
```
Comment:
```
Constructs a new exception with the specified detail message, cause, and bean for jax-ws exception serialization.
```
---
id: 22

Code snippet:
```
public Door(final Material type,BlockFace face,boolean isOpen){
  super(type);
  setTopHalf(false);
  setFacingDirection(face);
  setOpen(isOpen);
}
```
Comment:
```
Constructs the bottom half of a door of the given material type, facing the specified direction and set to open or closed.
```
---
id: 23

Code snippet:
```
public PlaSegmentFloat(PlaPointFloat p_a,PlaPointFloat p_b){
  point_a=check_input(p_a);
  point_b=check_input(p_b);
  is_nan|=point_a.equals(point_b);
}
```
Comment:
```
Creates a line from two floatpoints if null points or the same point is given then the segment will be a nan.
```
---
id: 24

Code snippet:
```
public boolean hasEvents(){
  return !events.isEmpty();
}
```
Comment:
```
Returns whether it has the event.
```
---
id: 25

Code snippet:
```
public static UIViewRoot createView(final String viewId){
  final FacesContext facesContext=FacesContext.getCurrentInstance();
  final ViewHandler viewHandler=facesContext.getApplication().getViewHandler();
  final UIViewRoot view=viewHandler.createView(facesContext,viewId);
  try {
    viewHandler.getViewDeclarationLanguage(facesContext,viewId).buildView(facesContext,view);
  }
 catch (  final IOException e) {
    throw new RuntimeException(e);
  }
  return view;
}
```
Comment:
```
Creates and returns a new view.
```
---
id: 26

Code snippet:
```
public void test_ConstructorLjava_lang_StringLjava_text_DateFormatSymbols(){
  DateFormatSymbols symbols=new DateFormatSymbols(Locale.ENGLISH);
  symbols.setEras(new String[]{\"Before\",\"After\"});
  SimpleDateFormat f2=new SimpleDateFormat(\"y\'y\'yy\",symbols);
  assertTrue(\"Wrong class\",f2.getClass() == SimpleDateFormat.class);
  assertEquals(\"Wrong pattern\",\"y\'y\'yy\",f2.toPattern());
  assertTrue(\"Wrong symbols\",f2.getDateFormatSymbols().equals(symbols));
  assertTrue(\"Doesn\'t work\",f2.format(new Date()).getClass() == String.class);
  try {
    new SimpleDateFormat(null,symbols);
    fail(\"NullPointerException was not thrown.\");
  }
 catch (  NullPointerException npe) {
  }
  try {
    new SimpleDateFormat(\"eee\",symbols);
    fail(\"IllegalArgumentException was not thrown.\");
  }
 catch (  IllegalArgumentException iae) {
  }
}
```
Comment:
```
Java.text.simpledateformat#simpledateformat(java.lang.string, java.text.dateformatsymbols).
```
---
id: 27

Code snippet:
```
public void removeOperation(Operation operation){
  if (isRunning) {
    if (operationHandlerThreadHandler == null)     return;
    operationHandlerThreadHandler.removeCallbacks(new AndroidOperation(this,operation));
  }
 else {
    operationQueue.remove(new AndroidOperation(this,operation));
  }
}
```
Comment:
```
Remove any pending operations that are in operationqueue.
```
---
id: 28

Code snippet:
```
public LineString asLineString(int precision){
  return LineString.fromPolyline(getGeometry(),precision);
}
```
Comment:
```
Gets a geojson linestring which can be used to get route coordinates useful for drawing on a map view.
```
---
id: 29

Code snippet:
```
public boolean equals(String obj2){
  return str().equals(obj2);
}
```
Comment:
```
Compares this string to the specified <code>string</code>. the result is <code>true</code> if and only if the argument is not <code>null</code> and is a <code>string</code> object that represents the same sequence of characters as this object.
```
---
id: 30

Code snippet:
```
@Override protected void constructApplication(String[] args){
  try {
    controlPanel=new ControlPanel();
    controlPanel.initialize(args);
  }
 catch (  Throwable t) {
    if (ControlPanelLog.isInitialized()) {
      logger.error(LocalizableMessage.raw(\"Error launching GUI: \" + t,t));
    }
    InternalError error=new InternalError(\"Failed to invoke initialize method\");
    error.initCause(t);
    throw error;
  }
}
```
Comment:
```
Called when the activity is first created.
```
---
id: 31

Code snippet:
```
public void testPosPosFirstShorter(){
  byte aBytes[]={-2,-3,-4,-4,5,14,23,39,48,57,66,5,14,23};
  byte bBytes[]={-128,9,56,100,-2,-76,89,45,91,3,-15,35,26,-117,23,87,-25,-75};
  int aSign=1;
  int bSign=1;
  byte rBytes[]={0,-2,-76,88,44,1,2,17,35,16,9,2,5,6,21};
  BigInteger aNumber=new BigInteger(aSign,aBytes);
  BigInteger bNumber=new BigInteger(bSign,bBytes);
  BigInteger result=aNumber.and(bNumber);
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
Flipbit(int n) outside a negative number.
```
---
id: 32

Code snippet:
```
public DiskFileItemFactory(){
  this(DEFAULT_SIZE_THRESHOLD,null);
}
```
Comment:
```
Creates a new instance.
```
---
id: 33

Code snippet:
```
private void readObject(ObjectInputStream s) throws ClassNotFoundException, IOException, HeadlessException {
  GraphicsEnvironment.checkHeadless();
  s.defaultReadObject();
  Object keyOrNull;
  while (null != (keyOrNull=s.readObject())) {
    String key=((String)keyOrNull).intern();
    if (itemListenerK == key)     addItemListener((ItemListener)(s.readObject()));
 else     if (actionListenerK == key)     addActionListener((ActionListener)(s.readObject()));
 else     s.readObject();
  }
}
```
Comment:
```
Reads the <code>objectinputstream</code> and if it isn\'t <code>null</code> adds a listener to receive both item events and action events (as specified by the key stored in the stream) fired by the <code>list</code>. unrecognized keys or values will be ignored.
```
---
id: 34

Code snippet:
```
public SearchResultReference(String referralURL){
  referralURLs=CollectionUtils.newArrayList(referralURL);
  this.controls=new ArrayList<>(0);
}
```
Comment:
```
Creates a new instance.
```
---
id: 35

Code snippet:
```
public BooleanByte(String identifier,AbstractTagFrameBody frameBody,int bitPosition){
  super(identifier,frameBody);
  if ((bitPosition < 0) || (bitPosition > 7)) {
    throw new IndexOutOfBoundsException(\"Bit position needs to be from 0 - 7 : \" + bitPosition);
  }
  this.bitPosition=bitPosition;
}
```
Comment:
```
Creates a new tag.
```
---
id: 36

Code snippet:
```
@Override public void toString(StringBuilder buffer){
  buffer.append(\"DeleteRequest(dn=\");
  buffer.append(dn);
  buffer.append(\")\");
}
```
Comment:
```
Adds a request to the request.
```
---
id: 37

Code snippet:
```
public Map mapToNativeEnvironment(Environment xacmlContextEnvironment,List xacmlContextSubjects) throws XACMLException {
  return null;
}
```
Comment:
```
Returns a map containing all the given elements, in the order they are returned by the collection\'s iterator.
```
---
id: 38

Code snippet:
```
public void testReceive_UnconnectedCloseNull() throws Exception {
  assertFalse(this.channel1.isConnected());
  this.channel1.close();
  assertFalse(this.channel1.isOpen());
  try {
    this.channel1.receive(null);
    fail(\"Should throw a NPE here.\");
  }
 catch (  NullPointerException e) {
  }
}
```
Comment:
```
Test method for \'datagramchannelimpl.receive(bytebuffer)\'.
```
---
id: 39

Code snippet:
```
public final boolean isSecure(Socket sock) throws IllegalArgumentException {
  if (sock == null) {
    throw new IllegalArgumentException(\"Socket may not be null.\");
  }
  if (sock.getClass() != Socket.class) {
    throw new IllegalArgumentException(\"Socket not created by this factory.\");
  }
  if (sock.isClosed()) {
    throw new IllegalArgumentException(\"Socket is closed.\");
  }
  return false;
}
```
Comment:
```
Returns true if field corresponding to fieldid is set (has been assigned a value) and false otherwise.
```
---
id: 40

Code snippet:
```
public void validateObject() throws InvalidObjectException {
  try {
    for (    JComponent root : roots) {
      SwingUtilities.updateComponentTreeUI(root);
    }
  }
  finally {
    readObjectCallbacks.remove(inputStream);
  }
}
```
Comment:
```
This is the method that\'s called after the entire graph of objects has been read in. it initializes the ui property of all of the copmonents with <code>swingutilities.updatecomponenttreeui</code>.
```
---
id: 41

Code snippet:
```
public InputMap(){
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
@Override public void execute(Context context,Map<String,Object> contextMap) throws ExecutionException {
  String invokerName=(String)contextMap.get(INVOKER_NAME);
  String scriptName=(String)contextMap.get(CONFIG_NAME);
  JsonValue params=new JsonValue(contextMap).get(CONFIGURED_INVOKE_CONTEXT);
  startTaskScanJob(context,invokerName,scriptName,params);
}
```
Comment:
```
Invoked by the task scanner whenever the task scanner is triggered by the scheduler.
```
---
id: 43

Code snippet:
```
private void postToTarget(RequestSecurityTokenResponse rstr,String targetURL) throws IOException, ServletException {
  String classMethod=\"IDPSSOUtil.postToTarget: \";
  String wresult=rstr.toString();
  if (debug.messageEnabled()) {
    debug.message(classMethod + \"wresult before encoding: \" + wresult);
  }
  request.setAttribute(WSFederationConstants.POST_ACTION,ESAPI.encoder().encodeForHTML(targetURL));
  request.setAttribute(WSFederationConstants.POST_WA,WSFederationConstants.WSIGNIN10);
  request.setAttribute(WSFederationConstants.POST_WCTX,ESAPI.encoder().encodeForHTML(wctx));
  request.setAttribute(WSFederationConstants.POST_WRESULT,ESAPI.encoder().encodeForHTML(wresult));
  request.getRequestDispatcher(\"/wsfederation/jsp/post.jsp\").forward(request,response);
}
```
Comment:
```
Called when a request is received.
```
---
id: 44

Code snippet:
```
private static JKSKeyProvider createKeyProvider(){
  JKSKeyProvider jksKp;
  if (useSpecificTrustStore()) {
    jksKp=new JKSKeyProvider(SOAP_KEYSTORE_FILE_PROP,SOAP_KEYSTORE_PASS_FILE_PROP,SOAP_KEYSTORE_TYPE_PROP,SOAP_PRIVATE_KEY_PASS_FILE_PROP);
  }
 else {
    jksKp=new JKSKeyProvider();
  }
  return jksKp;
}
```
Comment:
```
Creates a new instance of keypair.
```
---
id: 45

Code snippet:
```
public Builder withAccessKey(String accessKey){
  config.setAccessKey(accessKey);
  return this;
}
```
Comment:
```
Sets the key.
```
---
id: 46

Code snippet:
```
@Override public boolean isLoggable(LogRecord record){
  return super.isLoggable(record);
}
```
Comment:
```
Check if this <tt>handler</tt> would actually log a given <tt>logrecord</tt> into its internal buffer. <p> this method checks if the <tt>logrecord</tt> has an appropriate level and whether it satisfies any <tt>filter</tt>. however it does <b>not</b> check whether the <tt>logrecord</tt> would result in a \"push\" of the buffer contents. it will return false if the <tt>logrecord</tt> is null. <p>.
```
---
id: 47

Code snippet:
```
public synchronized BukkitTask runTaskTimer(Plugin plugin,long delay,long period) throws IllegalArgumentException, IllegalStateException {
  checkState();
  return setupId(Bukkit.getScheduler().runTaskTimer(plugin,(Runnable)this,delay,period));
}
```
Comment:
```
Schedules this to repeatedly run until cancelled, starting after the specified number of server ticks.
```
---
id: 48

Code snippet:
```
public void importSubConfig(String subConfigName,String exportedSubConfigName) throws SMSException, SSOException {
}
```
Comment:
```
Imports a service sub-configuration to the list of localy defined sub-configuration. the imported sub-configuration name must be fully qualified, as obtained from <code>getexportedsubconfignames</code>.
```
---
id: 49

Code snippet:
```
DynamicGroup(AttrSet attrSet) throws UMSException {
  this(TemplateManager.getTemplateManager().getCreationTemplate(_class,null),attrSet);
}
```
Comment:
```
Constructs a <code>dynamicgroup</code> in memory using the default registered template for <code>dynamicgroup</code>. this is an in-memory representation of a new object and one needs to call the <code>save</code> method to save this new object to persistent storage.
```
---
id: 50

Code snippet:
```
private static void scanPathRecursive(File dir,final StringBuilder sb,final int l){
  File[] files=dir.listFiles();
  if (files == null)   return;
  for (  File f : files) {
    if (f.isDirectory()) {
      scanPathRecursive(f,sb,l);
    }
 else     if (f.getName().endsWith(\".class\")) {
      sb.append(f.getAbsolutePath().substring(l)).append(\"
\");
    }
  }
}
```
Comment:
```
Scan path recursively.
```
---
id: 51

Code snippet:
```
public AMPostCallBackException(String msg,String errorCode,UMSException ue){
  super(msg,errorCode,ue);
}
```
Comment:
```
Constructs a new exception with the specified detail message. the cause is not initialized.
```
---
id: 52

Code snippet:
```
public static void checkContentLength(HttpServletRequest servletRequest) throws L10NMessageImpl {
  int length=servletRequest.getContentLength();
  if (length > maxContentLength) {
    Object[] args={new Integer(length),new Integer(maxContentLength)};
    throw new L10NMessageImpl(bundleName,\"contentLengthTooLarge\",args);
  }
 else {
    return;
  }
}
```
Comment:
```
Use this method to check an http servlet request size against the configured limit to insure that it is not too large, and possibly being sent to an openam servlet to cause a denial of service (dos).
```
---
id: 53

Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(hc_attrinsertbefore5.class,args);
}
```
Comment:
```
Runs this test from the command line.
```
---
id: 54

Code snippet:
```
protected boolean isToggleSelectionEvent(MouseEvent event){
  return (SwingUtilities.isLeftMouseButton(event) && BasicGraphicsUtils.isMenuShortcutKeyDown(event));
}
```
Comment:
```
Returns <code>true</code> if <code>mouseevent</code> is <code>true</code>.
```
---
id: 55

Code snippet:
```
private DiagnosticsAgent(){
}
```
Comment:
```
Prevents class instantiation.
```
---
id: 56

Code snippet:
```
public PlaPoint end_point(){
  return end_point;
}
```
Comment:
```
Returns the intersection of the last 2 lines of this segment.
```
---
id: 57

Code snippet:
```
public boolean update(Long dataFilterID,String dataFilterName,String dataFilterDisplayName,Long filterOnDataTypeID,Long compareWithDataTypeID){
  if (dataFilterID == null) {
    throw new IllegalArgumentException(\"primary key null.\");
  }
  ContentValues args=new ContentValues();
  if (dataFilterName != null) {
    args.put(KEY_DATAFILTERNAME,dataFilterName);
  }
  if (dataFilterDisplayName != null) {
    args.put(KEY_DATAFILTERDISPLAYNAME,dataFilterDisplayName);
  }
  if (filterOnDataTypeID != null) {
    args.put(KEY_FILTERONDATATYPEID,filterOnDataTypeID);
  }
  if (compareWithDataTypeID != null) {
    args.put(KEY_COMPAREWITHDATATYPEID,compareWithDataTypeID);
  }
  if (args.size() > 0) {
    return database.update(DATABASE_TABLE,args,KEY_DATAFILTERID + \"=\" + dataFilterID,null) > 0;
  }
  return false;
}
```
Comment:
```
Update a datafilter record with specific parameters.
```
---
id: 58

Code snippet:
```
protected synchronized void insertAttributeSetAt(AttributeSet as,int index){
  int numAttrs=attrs.length;
  AttributeSet newAttrs[]=new AttributeSet[numAttrs + 1];
  if (index < numAttrs) {
    if (index > 0) {
      System.arraycopy(attrs,0,newAttrs,0,index);
      System.arraycopy(attrs,index,newAttrs,index + 1,numAttrs - index);
    }
 else {
      System.arraycopy(attrs,0,newAttrs,1,numAttrs);
    }
  }
 else {
    System.arraycopy(attrs,0,newAttrs,0,numAttrs);
  }
  newAttrs[index]=as;
  attrs=newAttrs;
}
```
Comment:
```
Inserts the specified attribute at the specified index in the list. each component in this vector with an index greater or equal to the specified index is shifted upward to have an index one greater than the value it had previously.
```
---
id: 59

Code snippet:
```
static StringBuilder appendQuotedString(StringBuilder target,String key){
  target.append(\'\"\');
  for (int i=0, len=key.length(); i < len; i++) {
    char ch=key.charAt(i);
switch (ch) {
case \'
\':
      target.append(\"%0A\");
    break;
case \'\r\':
  target.append(\"%0D\");
break;
case \'\"\':
target.append(\"%22\");
break;
default :
target.append(ch);
break;
}
}
target.append(\'\"\');
return target;
}
```
Comment:
```
Appends a quoted-string to a stringbuilder. <p>rfc 2388 is rather vague about how one should escape special characters in form-data parameters, and as it turns out firefox and chrome actually do rather different things, and both say in their comments that they\'re not really sure what the right approach is. we go with chrome\'s behavior (which also experimentally seems to match what ie does), but if you actually want to have a good chance of things working, please avoid double-quotes, newlines, percent signs, and the like in your field names.
```
---
id: 60

Code snippet:
```
public void testConstrDoubleMathContext(){
  double a=732546982374982347892379283571094797.287346782359284756;
  int precision=21;
  RoundingMode rm=RoundingMode.CEILING;
  MathContext mc=new MathContext(precision,rm);
  String res=\"732546982374982285074\";
  int resScale=-15;
  BigDecimal result=new BigDecimal(a,mc);
  assertEquals(\"incorrect value\",res,result.unscaledValue().toString());
  assertEquals(\"incorrect scale\",resScale,result.scale());
}
```
Comment:
```
New bigdecimal(double value, mathcontext).
```
---
id: 61

Code snippet:
```
public boolean isCellEditable(EventObject anEvent){
  if (anEvent instanceof MouseEvent) {
    return ((MouseEvent)anEvent).getClickCount() >= clickCountToStart;
  }
  return true;
}
```
Comment:
```
Returns true if <code>anevent</code> is <b>not</b> a <code>mouseevent</code>. otherwise, it returns true if the necessary number of clicks have occurred, and returns false otherwise.
```
---
id: 62

Code snippet:
```
public static boolean hasClass(MavenProject project,String... classNames){
  URLClassLoader compileClassLoader=getCompileClassLoader(project);
  for (  String className : classNames) {
    try {
      compileClassLoader.loadClass(className);
      return true;
    }
 catch (    Throwable e) {
    }
  }
  return false;
}
```
Comment:
```
Checks whether the given class is a java class.
```
---
id: 63

Code snippet:
```
public NASPortTypeAttribute(int portType){
  super(OctetUtils.toOctets(AttributeType.NAS_PORT_TYPE,portType));
  this.portType=portType;
}
```
Comment:
```
Creates a new attribute.
```
---
id: 64

Code snippet:
```
public SASLResponse(String statusCode){
  this.statusCode=statusCode;
}
```
Comment:
```
Instantiates a new response.
```
---
id: 65

Code snippet:
```
private void handleNonCORS(final HttpServletRequest request,final HttpServletResponse response,final FilterChain filterChain) throws IOException, ServletException {
  filterChain.doFilter(request,response);
}
```
Comment:
```
Handles the http <code>get</code> method.
```
---
id: 66

Code snippet:
```
public SDPAnnounceParser(Vector sdpMessage){
  this.sdpMessage=sdpMessage;
}
```
Comment:
```
Creates new sdpannounceparser.
```
---
id: 67

Code snippet:
```
public long bytesUsed() throws IOException {
  return diskLruCache.size();
}
```
Comment:
```
User should be sure there are no outstanding operations.
```
---
id: 68

Code snippet:
```
public static List sortItems(Collection collection,Locale locale){
  List sorted=Collections.EMPTY_LIST;
  if ((collection != null) && !collection.isEmpty()) {
    sorted=new ArrayList(collection);
    Collator collator=Collator.getInstance(locale);
    Collections.sort(sorted,collator);
  }
  return sorted;
}
```
Comment:
```
Sorts the given collection of items in the given collection, using the given comparator.
```
---
id: 69

Code snippet:
```
@Override public boolean equals(Object obj){
  if (obj == null) {
    return false;
  }
  if (getClass() != obj.getClass()) {
    return false;
  }
  final Table other=(Table)obj;
  if (!Objects.equals(this.database,other.database)) {
    return false;
  }
  if (!Objects.equals(this.name,other.name)) {
    return false;
  }
  if (!Objects.equals(this.description,other.description)) {
    return false;
  }
  if (this.getTtl() != other.getTtl()) {
    return false;
  }
  if (this.getDeleteTtl() != other.getDeleteTtl()) {
    return false;
  }
  return true;
}
```
Comment:
```
Tests this instance for equality with an arbitrary object.
```
---
id: 70

Code snippet:
```
public void test_PBKDF2_b8312059() throws Exception {
  char[] password=\"\u0141\u0142\".toCharArray();
  byte[] salt=\"salt\".getBytes();
  int iterations=4096;
  int keyLength=160;
  byte[] expected_utf8=new byte[]{(byte)0x4c,(byte)0xe0,(byte)0x6a,(byte)0xb8,(byte)0x48,(byte)0x04,(byte)0xb7,(byte)0xe7,(byte)0x72,(byte)0xf2,(byte)0xaf,(byte)0x5e,(byte)0x54,(byte)0xe9,(byte)0x03,(byte)0xad,(byte)0x59,(byte)0x64,(byte)0x8b,(byte)0xab};
  byte[] expected_8bit=new byte[]{(byte)0x6e,(byte)0x43,(byte)0xe0,(byte)0x18,(byte)0xc5,(byte)0x50,(byte)0x0d,(byte)0xa7,(byte)0xfe,(byte)0x7a,(byte)0x44,(byte)0x4d,(byte)0x99,(byte)0x5d,(byte)0x8c,(byte)0xae,(byte)0xc1,(byte)0xc9,(byte)0x17,(byte)0xce};
  test_PBKDF2_UTF8(password,salt,iterations,keyLength,expected_utf8);
  test_PBKDF2_8BIT(password,salt,iterations,keyLength,expected_8bit);
}
```
Comment:
```
Test for <code>getcount()</code> method.
```
---
id: 71

Code snippet:
```
public void test_readFully$B_writeBytesLjava_lang_String() throws IOException {
  byte[] buf=new byte[testLength];
  RandomAccessFile raf=new java.io.RandomAccessFile(fileName,\"rw\");
  raf.writeBytes(testString);
  raf.seek(0);
  try {
    raf.readFully(null);
    fail(\"Test 1: NullPointerException expected.\");
  }
 catch (  NullPointerException e) {
  }
  raf.readFully(buf);
  assertEquals(\"Test 2: Incorrect bytes written or read;\",testString,new String(buf));
  try {
    raf.readFully(buf);
    fail(\"Test 3: EOFException expected.\");
  }
 catch (  EOFException e) {
  }
  raf.close();
  try {
    raf.writeBytes(\"Already closed.\");
    fail(\"Test 4: IOException expected.\");
  }
 catch (  IOException e) {
  }
  try {
    raf.readFully(buf);
    fail(\"Test 5: IOException expected.\");
  }
 catch (  IOException e) {
  }
}
```
Comment:
```
Java.io.randomaccessfile#writebytes(java.lang.string) java.io.randomaccessfile#readfully(byte[]).
```
---
id: 72

Code snippet:
```
public static boolean match(String name,int majorVersion,int minorVersion){
  return osName.equalsIgnoreCase(name) && (osMajorVersion == majorVersion) && (osMinorVersion == minorVersion);
}
```
Comment:
```
Returns true if the given version is greater than or equal to the given version.
```
---
id: 73

Code snippet:
```
@Override public void onNewIntent(final Intent intent){
  delegate.onNewIntent(intent);
}
```
Comment:
```
Called when the activity is first created.
```
---
id: 74

Code snippet:
```
static String keyToDNString(ByteString key){
  return key.toByteString().toASCIIString();
}
```
Comment:
```
Converts a string to a byte array.
```
---
id: 75

Code snippet:
```
private boolean validateResourceNamesUsingRegex(String resource,Set<String> regexPatterns,RegExResourceName resourceHandler){
  for (  String regex : regexPatterns) {
    ResourceMatch match=resourceHandler.compare(regex,resource,true);
    if (match == ResourceMatch.EXACT_MATCH || match == ResourceMatch.WILDCARD_MATCH || match == ResourceMatch.SUB_RESOURCE_MATCH) {
      return true;
    }
  }
  return false;
}
```
Comment:
```
Verifies a resource against the set of allowed regex patterns with help from the regex resource handler.
```
---
id: 76

Code snippet:
```
public boolean seek(int index){
  org.omg.CORBA.portable.ServantObject $so=_servant_preinvoke(\"seek\",_opsClass);
  DynStructOperations $self=(DynStructOperations)$so.servant;
  try {
    return $self.seek(index);
  }
  finally {
    _servant_postinvoke($so);
  }
}
```
Comment:
```
Sets the current position to index. the current position is indexed 0 to n-1, that is, index zero corresponds to the first component. the operation returns true if the resulting current position indicates a component of the dynany and false if index indicates a position that does not correspond to a component. calling seek with a negative index is legal. it sets the current position to -1 to indicate no component and returns false. passing a non-negative index value for a dynany that does not have a component at the corresponding position sets the current position to -1 and returns false.
```
---
id: 77

Code snippet:
```
public void attributeDecl(String eName,String aName,String type,String valueDefault,String value) throws SAXException {
}
```
Comment:
```
This method does nothing.
```
---
id: 78

Code snippet:
```
public String generateDetailedUpgradeReport(SSOToken adminToken,boolean html){
  String delimiter=html ? HTML_BR : TXT_LF;
  Map<String,String> tags=new HashMap<String,String>();
  tags.put(LF,delimiter);
  tags.put(CREATED_DATE,createdDate);
  tags.put(EXISTING_VERSION,existingVersion);
  tags.put(NEW_VERSION,VersionUtils.getWarFileVersion());
  StringBuilder report=new StringBuilder(tagSwapReport(tags,\"report\"));
  for (  UpgradeStep upgradeStep : upgradeSteps) {
    report.append(upgradeStep.getDetailedReport(delimiter)).append(delimiter);
  }
  return report.toString();
}
```
Comment:
```
Generates a tag with the given parameters.
```
---
id: 79

Code snippet:
```
protected Source processSource(StylesheetHandler handler,Source source){
  return source;
}
```
Comment:
```
This method does nothing, but a class that extends this class could over-ride it and do some processing of the source.
```
---
id: 80

Code snippet:
```
@Override public Foo findByUuid_First(String uuid,OrderByComparator<Foo> orderByComparator) throws NoSuchFooException {
  Foo foo=fetchByUuid_First(uuid,orderByComparator);
  if (foo != null) {
    return foo;
  }
  StringBundler msg=new StringBundler(4);
  msg.append(_NO_SUCH_ENTITY_WITH_KEY);
  msg.append(\"uuid=\");
  msg.append(uuid);
  msg.append(StringPool.CLOSE_CURLY_BRACE);
  throw new NoSuchFooException(msg.toString());
}
```
Comment:
```
Fetch a string.
```
---
id: 81

Code snippet:
```
public int length(){
  return n;
}
```
Comment:
```
Obtain number of items in array.
```
---
id: 82

Code snippet:
```
public boolean isSessionEncrypted(){
  final Session session=connectedRS.get().session;
  return session != null ? session.isEncrypted() : false;
}
```
Comment:
```
Determine whether the connection to the replication server is encrypted.
```
---
id: 83

Code snippet:
```
public Hashtable parseLogsFromDebugFile(String logFileName){
  try {
    File file=new File(logFileName);
    long length=file.length();
    char[] cbuf=new char[(int)length];
    FileReader fr=new FileReader(file);
    fr.read(cbuf);
    fr.close();
    StringBuffer sb=new StringBuffer();
    sb.append(\"<?xml version=\'1.0\' encoding=\'us-ascii\'?>
\").append(\"<messages>
\").append(new String(cbuf)).append(\"]]></debug></messages>
\");
    InputSource inputSource=new InputSource(new ByteArrayInputStream(sb.toString().getBytes()));
    return this.parseLogs(inputSource);
  }
 catch (  IOException ex) {
    ex.printStackTrace();
    return null;
  }
}
```
Comment:
```
Generate a file that can be digested by the trace viewer.
```
---
id: 84

Code snippet:
```
public int length(){
  return m_length;
}
```
Comment:
```
Returns the length of the array.
```
---
id: 85

Code snippet:
```
public String jmxHost(){
  return values.jmxHost;
}
```
Comment:
```
Returns a string representation of this object.
```
---
id: 86

Code snippet:
```
public synchronized void put(K k,V v){
  Reject.ifNull(k,v);
  K previousValue=reverse.get(v);
  if (previousValue != null) {
    map.remove(previousValue);
  }
  map.put(k,v);
  reverse.put(v,k);
}
```
Comment:
```
Store a mapping of key to value. note: if there was a previous mapping for value, this will be cleaned up. synchronized: to ensure both maps are updated in an atomic way.
```
---
id: 87

Code snippet:
```
static int findDNKeyParent(ByteSequence dnKey){
  if (dnKey.length() == 0) {
    return -1;
  }
  for (int i=dnKey.length() - 1; i >= 0; i--) {
    if (positionIsRDNSeparator(dnKey,i)) {
      return i;
    }
  }
  return 0;
}
```
Comment:
```
Finds the key for the given key.
```
---
id: 88

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
Puts an element into the cache.
```
---
id: 89

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
id: 90

Code snippet:
```
void clearSubjectResultCache(String tokenIdString) throws PolicyException {
  if (PolicyManager.debug.messageEnabled()) {
    PolicyManager.debug.message(\"Subjects.clearSubjectResultCache(tokenIdString): \" + \" clearing cached subject evaluation result for \" + \" tokenId XXXXX\");
  }
  resultCache.remove(tokenIdString);
}
```
Comment:
```
Clears the cached membership evaluation results corresponding to the <code>tokenidstring</code>. this is triggered through <code>policyssotokenlistener</code>, <code>policycache</code> and <code>policy</code> when session property of a logged in user is changed.
```
---
id: 91

Code snippet:
```
public void remove(String jwt){
  sessionInfoCache.remove(jwt);
}
```
Comment:
```
Removes a session from the cache.
```
---
id: 92

Code snippet:
```
protected void addExtension(final String extension){
  if (extension != null) {
    if (extensions == null) {
      extensions=new Vector<>();
    }
    extensions.add(extension);
  }
}
```
Comment:
```
Add a extension with the given extension.
```
---
id: 93

Code snippet:
```
public final DetectorResult detect(Map<DecodeHintType,?> hints) throws NotFoundException, FormatException {
  resultPointCallback=hints == null ? null : (ResultPointCallback)hints.get(DecodeHintType.NEED_RESULT_POINT_CALLBACK);
  FinderPatternFinder finder=new FinderPatternFinder(image,resultPointCallback);
  FinderPatternInfo info=finder.find(hints);
  return processFinderPatternInfo(info);
}
```
Comment:
```
<p>detects a qr code in an image.</p>.
```
---
id: 94

Code snippet:
```
int readUtah(int row,int column,int numRows,int numColumns){
  int currentByte=0;
  if (readModule(row - 2,column - 2,numRows,numColumns)) {
    currentByte|=1;
  }
  currentByte<<=1;
  if (readModule(row - 2,column - 1,numRows,numColumns)) {
    currentByte|=1;
  }
  currentByte<<=1;
  if (readModule(row - 1,column - 2,numRows,numColumns)) {
    currentByte|=1;
  }
  currentByte<<=1;
  if (readModule(row - 1,column - 1,numRows,numColumns)) {
    currentByte|=1;
  }
  currentByte<<=1;
  if (readModule(row - 1,column,numRows,numColumns)) {
    currentByte|=1;
  }
  currentByte<<=1;
  if (readModule(row,column - 2,numRows,numColumns)) {
    currentByte|=1;
  }
  currentByte<<=1;
  if (readModule(row,column - 1,numRows,numColumns)) {
    currentByte|=1;
  }
  currentByte<<=1;
  if (readModule(row,column,numRows,numColumns)) {
    currentByte|=1;
  }
  return currentByte;
}
```
Comment:
```
Reads a local variable of the given local variable.
```
---
id: 95

Code snippet:
```
public void fatalError(SAXParseException e) throws SAXException {
  throw e;
}
```
Comment:
```
Receive notification of a recoverable error. <p>by default, do nothing. application writers may override this method in a subclass to take specific actions for each error, such as inserting the message in a log file or printing it to the console.</p>.
```
---
id: 96

Code snippet:
```
public void addHeader(@NonNull View view){
  if (view == null) {
    throw new IllegalArgumentException(\"You can\'t have a null header!\");
  }
  mHeaders.add(view);
}
```
Comment:
```
Add a fixed view to appear at the top of the grid. if addheaderview is called more than once, the views will appear in the order they were added. views added using this call can take focus if they want. <p> note: call this before calling setadapter. this is so headergridview can wrap the supplied cursor with one that will also account for header views.
```
---
id: 97

Code snippet:
```
public synchronized int indexOf(Object object,int location){
  if (object != null) {
    for (int i=location; i < elementCount; i++) {
      if (object.equals(elementData[i])) {
        return i;
      }
    }
  }
 else {
    for (int i=location; i < elementCount; i++) {
      if (elementData[i] == null) {
        return i;
      }
    }
  }
  return -1;
}
```
Comment:
```
Searches in this vector for the index of the specified object. the search for the object starts at the specified location and moves towards the end of this vector.
```
---
id: 98

Code snippet:
```
public PrivateMLet(URL[] urls,ClassLoader parent,URLStreamHandlerFactory factory,boolean delegateToCLR){
  super(urls,parent,factory,delegateToCLR);
}
```
Comment:
```
Creates a new urlclassloader.
```
---
id: 99

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
