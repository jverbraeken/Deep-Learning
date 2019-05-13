id: 200

Code snippet:
```
public String endTblDataActionDefaultHrefDisplay(ChildContentDisplayEvent event){
  String lbl=(String)tblModel.getValue(TBL_DATA_ACTION_DEFAULT_LABEL);
  return ((lbl != null) && (lbl.length() > 0)) ? event.getContent() : \"\";
}
```
Comment:
```
This method gets called when a button is clicked.
```
---
id: 201

Code snippet:
```
public void skippedEntity(String name) throws SAXException {
}
```
Comment:
```
Receive notification of a skipped entity.
```
---
id: 202

Code snippet:
```
@Override public Foo fetchByField2_First(boolean field2,OrderByComparator<Foo> orderByComparator){
  List<Foo> list=findByField2(field2,0,1,orderByComparator);
  if (!list.isEmpty()) {
    return list.get(0);
  }
  return null;
}
```
Comment:
```
Returns the first foo in the ordered set where field2 = &#63;.
```
---
id: 203

Code snippet:
```
public List<MappedMember> findFieldsByDesc(String text){
  List<MappedMember> list=new ArrayList<MappedMember>();
  for (  MappedMember mm : getFields()) {
    if (mm.getDesc().equals(text)) {
      list.add(mm);
    }
  }
  return list;
}
```
Comment:
```
Returns a list of fields matching a given descriptor.
```
---
id: 204

Code snippet:
```
public int corner_count(){
  return polyline.corner_count();
}
```
Comment:
```
returns the number of corners of this trace
```
---
id: 205

Code snippet:
```
public int size(){
  return count;
}
```
Comment:
```
Returns the number of bytes currently being used to store the values in this cache. This may be greater than the max size if a background deletion is pending.
```
---
id: 206

Code snippet:
```
public Status createStatus(Element elem) throws XACMLException {
  Object object=XACMLSDKUtils.getObjectInstance(XACMLConstants.STATUS,elem);
  if (object == null) {
    return new StatusImpl(elem);
  }
 else {
    return (Status)object;
  }
}
```
Comment:
```
<!-- begin-user-doc --> <!-- end-user-doc -->
```
---
id: 207

Code snippet:
```
@Override public String toString(){
  StringBuilder sb=new StringBuilder(\"ContextResource[\");
  sb.append(\"name=\");
  sb.append(getName());
  if (getDescription() != null) {
    sb.append(\", description=\");
    sb.append(getDescription());
  }
  if (getType() != null) {
    sb.append(\", type=\");
    sb.append(getType());
  }
  if (auth != null) {
    sb.append(\", auth=\");
    sb.append(auth);
  }
  if (scope != null) {
    sb.append(\", scope=\");
    sb.append(scope);
  }
  sb.append(\"]\");
  return (sb.toString());
}
```
Comment:
```
String Representation
```
---
id: 208

Code snippet:
```
@Override public List<Foo> findByField2(boolean field2){
  return findByField2(field2,QueryUtil.ALL_POS,QueryUtil.ALL_POS,null);
}
```
Comment:
```
Returns all the foos where field2 = &#63;.
```
---
id: 209

Code snippet:
```
public com.sun.identity.saml2.jaxb.metadata.CompanyElement createCompanyElement() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.saml2.jaxb.metadata.impl.CompanyElementImpl();
}
```
Comment:
```
<!-- begin-user-doc --> <!-- end-user-doc -->
```
---
id: 210

Code snippet:
```
public String resolveFrom(OAuth2Request request){
  AccessToken accessToken=request.getToken(AccessToken.class);
  String realm;
  if (accessToken != null) {
    realm=accessToken.getRealm();
  }
 else {
    realm=request.getParameter(RestletRealmRouter.REALM);
  }
  return realm;
}
```
Comment:
```
Resolve realm from the request
```
---
id: 211

Code snippet:
```
@Override public void startIntentSenderFromFragment(final Fragment fragment,final IntentSender intent,final int requestCode,@Nullable final Intent fillInIntent,final int flagsMask,final int flagsValues,final int extraFlags,final Bundle options) throws IntentSender.SendIntentException {
  try {
    delegate.startIntentSenderFromFragment(fragment,intent,requestCode,fillInIntent,flagsMask,flagsValues,extraFlags,options);
  }
 catch (  SuppressedException e) {
    throw (IntentSender.SendIntentException)e.getCause();
  }
}
```
Comment:
```
Called by Fragment.startIntentSenderForResult() to implement its behavior.
```
---
id: 212

Code snippet:
```
public MapDemo(Channel channel,String mapName){
  map=new LazyReplicatedMap<>(null,channel,5000,mapName,null);
  table=SimpleTableDemo.createAndShowGUI(map,channel.getLocalMember(false).getName());
  channel.addChannelListener(this);
  channel.addMembershipListener(this);
  this.messageReceived(null,null);
}
```
Comment:
```
Creates a new instance of this class.
```
---
id: 213

Code snippet:
```
@Deprecated public void logrb(Level level,String sourceClass,String sourceMethod,String bundleName,String msg,Throwable thrown){
  if (!isLoggable(level)) {
    return;
  }
  LogRecord lr=new LogRecord(level,msg);
  lr.setSourceClassName(sourceClass);
  lr.setSourceMethodName(sourceMethod);
  lr.setThrown(thrown);
  doLog(lr,bundleName);
}
```
Comment:
```
Log a message, specifying source class, method, and resource bundle name, with associated Throwable information. <p> If the logger is currently enabled for the given message level then the given arguments are stored in a LogRecord which is forwarded to all registered output handlers. <p> The msg string is localized using the named resource bundle.  If the resource bundle name is null, or an empty String or invalid then the msg string is not localized. <p> Note that the thrown argument is stored in the LogRecord thrown property, rather than the LogRecord parameters property.  Thus it is processed specially by output Formatters and is not treated as a formatting parameter to the LogRecord message property. <p>
```
---
id: 214

Code snippet:
```
public static String formatMessage(String formatStr,Object obj1){
  Object arr[]=new Object[1];
  arr[0]=obj1;
  return MessageFormat.format(formatStr,arr);
}
```
Comment:
```
Formats the given message.
```
---
id: 215

Code snippet:
```
void shrink(){
  int n=m_opMap.elementAt(MAPINDEX_LENGTH);
  m_opMap.setToSize(n + 4);
  m_opMap.setElementAt(0,n);
  m_opMap.setElementAt(0,n + 1);
  m_opMap.setElementAt(0,n + 2);
  n=m_tokenQueue.size();
  m_tokenQueue.setToSize(n + 4);
  m_tokenQueue.setElementAt(null,n);
  m_tokenQueue.setElementAt(null,n + 1);
  m_tokenQueue.setElementAt(null,n + 2);
}
```
Comment:
```
Replace the large arrays with a small array.
```
---
id: 216

Code snippet:
```
public static Bitmap createIconBitmap(String packageName,String resourceName,Context context){
  PackageManager packageManager=context.getPackageManager();
  try {
    Resources resources=packageManager.getResourcesForApplication(packageName);
    if (resources != null) {
      final int id=resources.getIdentifier(resourceName,null,null);
      return createIconBitmap(resources.getDrawableForDensity(id,LauncherAppState.getInstance().getInvariantDeviceProfile().fillResIconDpi),context);
    }
  }
 catch (  Exception e) {
  }
  return null;
}
```
Comment:
```
Returns a bitmap suitable for the all apps view. If the package or the resource do not exist, it returns null.
```
---
id: 217

Code snippet:
```
private void checkPermission(final String name,final Node configNode,final ServiceConfig permissionsConfig) throws SMSException, SSOException {
  final ServiceConfig permissionConfig=permissionsConfig.getSubConfig(name);
  if (permissionConfig == null) {
    newPermissions.add(ChangeSet.newInstance(name,configNode));
  }
}
```
Comment:
```
Given the permission name identifies whether that permission already exists. If it doesn\'t it registers creation of a new privilege.
```
---
id: 218

Code snippet:
```
public InitialLdapContext() throws NamingException {
  super(null);
}
```
Comment:
```
Constructs a new exception with <code>null</code> as its detail message. The cause is not initialized.
```
---
id: 219

Code snippet:
```
public StatusCode createStatusCode() throws XACMLException {
  Object object=XACMLSDKUtils.getObjectInstance(XACMLConstants.STATUS_CODE);
  if (object == null) {
    return new StatusCodeImpl();
  }
 else {
    return (StatusCode)object;
  }
}
```
Comment:
```
Returns a new instance of <code>StatusCode</code>.
```
---
id: 220

Code snippet:
```
@Override public int read() throws IOException {
  if (eof) {
    throw new IOException(\"Read after end of file\");
  }
  if (position == size) {
    return doEndOfFile();
  }
  position++;
  return processByte();
}
```
Comment:
```
Read a byte.
```
---
id: 221

Code snippet:
```
public LogVerifier(String log,AMPassword verPass){
  name=log;
  verPassword=verPass;
}
```
Comment:
```
Constructs a new exception with the specified detail message. The cause is not initialized.
```
---
id: 222

Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(namednodemapremovenameditemns04.class,args);
}
```
Comment:
```
Runs this test from the command line.
```
---
id: 223

Code snippet:
```
public EventReaderDelegate(){
}
```
Comment:
```
Construct an empty filter with no parent.
```
---
id: 224

Code snippet:
```
public static Collection<File> listFiles(File directory,IOFileFilter fileFilter,IOFileFilter dirFilter){
  validateListFilesParameters(directory,fileFilter);
  IOFileFilter effFileFilter=setUpEffectiveFileFilter(fileFilter);
  IOFileFilter effDirFilter=setUpEffectiveDirFilter(dirFilter);
  Collection<File> files=new java.util.LinkedList<File>();
  innerListFiles(files,directory,FileFilterUtils.or(effFileFilter,effDirFilter),false);
  return files;
}
```
Comment:
```
Finds files within a given directory (and optionally its subdirectories). All files found are filtered by an IOFileFilter. <p> If your search should recurse into subdirectories you can pass in an IOFileFilter for directories. You don\'t need to bind a DirectoryFileFilter (via logical AND) to this filter. This method does that for you. <p> An example: If you want to search through all directories called \"temp\" you pass in <code>FileFilterUtils.NameFileFilter(\"temp\")</code> <p> Another common usage of this method is find files in a directory tree but ignoring the directories generated CVS. You can simply pass in <code>FileFilterUtils.makeCVSAware(null)</code>.
```
---
id: 225

Code snippet:
```
private static boolean move(JsonValue subject,PatchOperation operation) throws BadRequestException {
  if (!operation.isMove()) {
    throw new BadRequestException(\"Operation is a \" + operation.getOperation() + \", not a move!\");
  }
  JsonValue value=subject.get(operation.getFrom());
  if (value == null || value.isNull()) {
    return false;
  }
  subject.remove(operation.getFrom());
  subject.add(operation.getField(),value.getObject());
  return true;
}
```
Comment:
```
Returns true if the specified value is valid.
```
---
id: 226

Code snippet:
```
public static double readSwappedDouble(InputStream input) throws IOException {
  return Double.longBitsToDouble(readSwappedLong(input));
}
```
Comment:
```
Reads a \"double\" value from an InputStream. The value is converted to the opposed endian system while reading.
```
---
id: 227

Code snippet:
```
public boolean preSendResponse(AuthnRequest authnRequest,String hostProviderID,String realm,HttpServletRequest request,HttpServletResponse response,Object session,String reqID,String relayState) throws SAML2Exception {
  return false;
}
```
Comment:
```
Perform a HTTP POST request and track the Android Context which initiated the request.
```
---
id: 228

Code snippet:
```
public SwallowedExceptionLogger(final Log log,final boolean logExpiredConnections){
  this.log=log;
  this.logExpiredConnections=logExpiredConnections;
}
```
Comment:
```
Create a SwallowedExceptionLogger with the given logger and expired connection logging property.
```
---
id: 229

Code snippet:
```
@NonNull public static Interpolator step(int first,int second){
  return join(constant(first),constant(second));
}
```
Comment:
```
Returns a new instance with the specified number of minutes added. <p> This instance is immutable and unaffected by this method call.
```
---
id: 230

Code snippet:
```
public static <T>ListIterator<T> emptyListIterator(){
  return Collections.<T>emptyList().listIterator();
}
```
Comment:
```
Returns an enumeration of all the available options..
```
---
id: 231

Code snippet:
```
ConfigurationError(String msg,Exception x){
  super(msg);
  this.exception=x;
}
```
Comment:
```
Construct a new instance with the specified detail string and exception.
```
---
id: 232

Code snippet:
```
public static float[] copyOfRange(float[] original,int from,int to){
  int newLength=to - from;
  if (newLength < 0)   throw new IllegalArgumentException(from + \" > \" + to);
  float[] copy=new float[newLength];
  System.arraycopy(original,from,copy,0,Math.min(original.length - from,newLength));
  return copy;
}
```
Comment:
```
Copies all elements in the specified array into a new array, from index start(inclusive) to end(exclusive). The first element (if any) in the new array is original[from], and other elements in the new array are in the original order. The padding value whose index is bigger than or equal to original.length - start is 0L.
```
---
id: 233

Code snippet:
```
@SuppressWarnings(\"unchecked\") @Override public PdfDictionary copyTo(PdfDocument document,boolean allowDuplicating){
  return (PdfDictionary)super.copyTo(document,allowDuplicating);
}
```
Comment:
```
Copies object to a specified document. Works only for objects that are read from existing document, otherwise an exception is thrown.
```
---
id: 234

Code snippet:
```
private void startConversationsClient(){
  if (mConversationsClient != null) {
    return;
  }
  mConversationsClient=TwilioConversationsClient.create(mAccessManager,conversationsClientListener());
  mConversationsClient.listen();
}
```
Comment:
```
Starts the server.
```
---
id: 235

Code snippet:
```
@Override @Test(expectedExceptions=IllegalBlockingModeException.class) public void testDecodeTruncatedLengthArrayAsEnumerated() throws Exception {
  super.testDecodeTruncatedLengthArrayAsEnumerated();
}
```
Comment:
```
Tests the <CODE>readEnumerated</CODE> method that takes a byte array with a truncated length array.
```
---
id: 236

Code snippet:
```
public float nextTabStop(float x,int tabOffset){
  if (getTabSet() == null && StyleConstants.getAlignment(getAttributes()) == StyleConstants.ALIGN_LEFT) {
    return getPreTab(x,tabOffset);
  }
  return super.nextTabStop(x,tabOffset);
}
```
Comment:
```
Returns the next tab stop position given a reference position. This view implements the tab coordinate system, and calls <code>getTabbedSpan</code> on the logical children in the process of layout to determine the desired span of the children.  The logical children can delegate their tab expansion upward to the paragraph which knows how to expand tabs. <code>LabelView</code> is an example of a view that delegates its tab expansion needs upward to the paragraph. <p> This is implemented to try and locate a <code>TabSet</code> in the paragraph element\'s attribute set.  If one can be found, its settings will be used, otherwise a default expansion will be provided.  The base location for for tab expansion is the left inset from the paragraphs most recent allocation (which is what the layout of the children is based upon).
```
---
id: 237

Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  NodeList addressList;
  Node testNode;
  NamedNodeMap attributes;
  Attr streetAttr;
  String value;
  doc=(Document)load(\"hc_staff\",true);
  addressList=doc.getElementsByTagName(\"acronym\");
  testNode=addressList.item(3);
  attributes=testNode.getAttributes();
  streetAttr=(Attr)attributes.getNamedItem(\"class\");
  streetAttr.setValue(\"Y&ent1;\");
  value=streetAttr.getValue();
  assertEquals(\"value\",\"Y&ent1;\",value);
  value=streetAttr.getNodeValue();
  assertEquals(\"nodeValue\",\"Y&ent1;\",value);
}
```
Comment:
```
Runs the test case.
```
---
id: 238

Code snippet:
```
public String toString(){
  return exp + \" like \" + new StringValueExp(pattern);
}
```
Comment:
```
Returns a string representation of this object.
```
---
id: 239

Code snippet:
```
public final void test_insertProviderAtLjava_security_ProviderLI(){
  try {
    Security.insertProviderAt(null,1);
    fail(\"No expected NullPointerException\");
  }
 catch (  NullPointerException e) {
  }
  Provider p=new MyProvider();
  int initNum=Security.getProviders().length;
  Provider initialSecondProviderName=Security.getProviders()[1];
  try {
    assertEquals(initNum + 1,Security.insertProviderAt(p,-1));
    assertSame(p,Security.getProviders()[initNum]);
    assertEquals(-1,Security.insertProviderAt(p,1));
    Security.removeProvider(p.getName());
    assertEquals(initNum + 1,Security.insertProviderAt(p,initNum + 100));
    assertSame(p,Security.getProviders()[initNum]);
    Security.removeProvider(p.getName());
    assertEquals(1,Security.insertProviderAt(p,1));
    assertSame(p,Security.getProviders()[0]);
    assertSame(initialSecondProviderName,Security.getProviders()[2]);
  }
  finally {
    Security.removeProvider(p.getName());
  }
}
```
Comment:
```
Adds a new element to the list.
```
---
id: 240

Code snippet:
```
public void uninstallUI(JComponent c){
  super.uninstallUI(c);
  MetalToolBarUI.unregister(c);
}
```
Comment:
```
Invokes the <code>uninstallUI</code> method on each UI handled by this object.
```
---
id: 241

Code snippet:
```
public Vertex addVertex(String label,List<DbDataContainer> attributes){
  Object[] attributesArray=new Object[(attributes.size() + 1) * 2];
  for (int i=1; i < attributes.size() + 1; i++) {
    attributesArray[2 * i]=attributes.get(i - 1).getField();
    attributesArray[2 * i + 1]=attributes.get(i - 1).getValue();
  }
  attributesArray[0]=T.label;
  attributesArray[1]=label;
  return this.graph.addVertex(attributesArray);
}
```
Comment:
```
Adds a list of attributes to the set.
```
---
id: 242

Code snippet:
```
public Scroller(Context context,Interpolator interpolator){
  this(context,interpolator,context.getApplicationInfo().targetSdkVersion >= Build.VERSION_CODES.HONEYCOMB);
}
```
Comment:
```
Creates a new Scroller.
```
---
id: 243

Code snippet:
```
@Override protected StringBuilder encodeBody(StringBuilder buffer){
  return buffer.append(method);
}
```
Comment:
```
Return body encoded in canonical form.
```
---
id: 244

Code snippet:
```
public static void main(String[] args){
  ControlPanelSplashScreen screen=new ControlPanelSplashScreen();
  screen.display(args);
}
```
Comment:
```
The main method for this class. It can be called from the event thread and outside the event thread.
```
---
id: 245

Code snippet:
```
public ReferToParser(String referTo){
  super(referTo);
}
```
Comment:
```
Creates a new instance.
```
---
id: 246

Code snippet:
```
public static WhoAmIExtendedResult copyOfWhoAmIExtendedResult(final WhoAmIExtendedResult result){
  return new WhoAmIExtendedResultImpl(result);
}
```
Comment:
```
Creates a copy of the given object.
```
---
id: 247

Code snippet:
```
public void process(final Query query){
  logger.trace(\"Processing query {}\",query);
  for (  Module module : modules) {
    module.process(query);
  }
}
```
Comment:
```
Called when a query is executed.
```
---
id: 248

Code snippet:
```
public void deregisterCallbackHandler(String id){
  eventManager.removeObjectChangeListener(id);
}
```
Comment:
```
De-Register a listener.
```
---
id: 249

Code snippet:
```
public void validate(){
}
```
Comment:
```
Checks the validity of the field.
```
---
id: 250

Code snippet:
```
public ELException(){
  super();
}
```
Comment:
```
<!-- begin-user-doc --> <!-- end-user-doc -->
```
---
id: 251

Code snippet:
```
public boolean equals(Object obj){
  return (obj != null && obj instanceof CompoundName && impl.equals(((CompoundName)obj).impl));
}
```
Comment:
```
Tests this instance for equality with an arbitrary object.
```
---
id: 252

Code snippet:
```
private boolean hasFallbackChildren(){
  for (ElemTemplateElement child=m_firstChild; child != null; child=child.m_nextSibling) {
    if (child.getXSLToken() == Constants.ELEMNAME_FALLBACK)     return true;
  }
  return false;
}
```
Comment:
```
Tell if this expression or it\'s subexpressions can traverse outside the current subtree.
```
---
id: 253

Code snippet:
```
private void initMetrics(ServletContext servletContext,EnumSet<DispatcherType> disps){
  log.debug(\"Initializing Metrics registries\");
  servletContext.setAttribute(InstrumentedFilter.REGISTRY_ATTRIBUTE,metricRegistry);
  servletContext.setAttribute(MetricsServlet.METRICS_REGISTRY,metricRegistry);
  log.debug(\"Registering Metrics Filter\");
  FilterRegistration.Dynamic metricsFilter=servletContext.addFilter(\"webappMetricsFilter\",new InstrumentedFilter());
  metricsFilter.addMappingForUrlPatterns(disps,true,\"/*\");
  metricsFilter.setAsyncSupported(true);
  log.debug(\"Registering Metrics Servlet\");
  ServletRegistration.Dynamic metricsAdminServlet=servletContext.addServlet(\"metricsServlet\",new MetricsServlet());
  metricsAdminServlet.addMapping(\"/management/jhipster/metrics/*\");
  metricsAdminServlet.setAsyncSupported(true);
  metricsAdminServlet.setLoadOnStartup(2);
}
```
Comment:
```
Initialize global variables
```
---
id: 254

Code snippet:
```
public ContainerEvent(Component source,int id,Component child){
  super(source,id);
  this.child=child;
}
```
Comment:
```
Constructs a <code>ContainerEvent</code> object. <p> This method throws an <code>IllegalArgumentException</code> if <code>source</code> is <code>null</code>.
```
---
id: 255

Code snippet:
```
public BindException(String msg){
  super(msg);
}
```
Comment:
```
Constructs a new BindException with the specified detail message as to why the bind error occurred. A detail message is a String that gives a specific description of this error.
```
---
id: 256

Code snippet:
```
protected void tearDown(){
  try {
    os.close();
  }
 catch (  Exception e) {
  }
  try {
    dis.close();
  }
 catch (  Exception e) {
  }
}
```
Comment:
```
Tear down instance variables required by this test case.
```
---
id: 257

Code snippet:
```
private void addInclude(Node parent,Collection<String> files) throws JasperException {
  if (files != null) {
    Iterator<String> iter=files.iterator();
    while (iter.hasNext()) {
      String file=iter.next();
      AttributesImpl attrs=new AttributesImpl();
      attrs.addAttribute(\"\",\"file\",\"file\",\"CDATA\",file);
      Node includeNode=new Node.IncludeDirective(attrs,reader.mark(),parent);
      processIncludeDirective(file,includeNode);
    }
  }
}
```
Comment:
```
Adds a new element to the set of matched elements.
```
---
id: 258

Code snippet:
```
public static String toString(InputStream input,String encoding) throws IOException {
  return toString(input,Charsets.toCharset(encoding));
}
```
Comment:
```
Get the contents of an <code>InputStream</code> as a String using the specified character encoding. <p> Character encoding names can be found at <a href=\"http://www.iana.org/assignments/character-sets\">IANA</a>. <p> This method buffers the input internally, so there is no need to use a <code>BufferedInputStream</code>.
```
---
id: 259

Code snippet:
```
public final static String formatStatusLine(final StatusLine statline,LineFormatter formatter){
  if (formatter == null)   formatter=BasicLineFormatter.DEFAULT;
  return formatter.formatStatusLine(null,statline).toString();
}
```
Comment:
```
Formats a status line.
```
---
id: 260

Code snippet:
```
public void testCase24(){
  byte rBytes[]={0};
  BigInteger aNumber=BigInteger.ONE;
  BigInteger bNumber=BigInteger.ONE;
  BigInteger result=aNumber.subtract(bNumber);
  byte resBytes[]=new byte[rBytes.length];
  resBytes=result.toByteArray();
  for (int i=0; i < resBytes.length; i++) {
    assertTrue(resBytes[i] == rBytes[i]);
  }
  assertEquals(0,result.signum());
}
```
Comment:
```
flipBit(int n) outside a negative number
```
---
id: 261

Code snippet:
```
@NonNull public final Agera observeOn(@NonNull Executor executor){
  return new AgeraObserveOnExecutor(this,executor,false);
}
```
Comment:
```
Makes sure update() signals are called on the specified Executor.
```
---
id: 262

Code snippet:
```
private void processJournal() throws IOException {
  deleteIfExists(journalFileTmp);
  for (Iterator<Entry> i=lruEntries.values().iterator(); i.hasNext(); ) {
    Entry entry=i.next();
    if (entry.currentEditor == null) {
      for (int t=0; t < valueCount; t++) {
        size+=entry.lengths[t];
      }
    }
 else {
      entry.currentEditor=null;
      for (int t=0; t < valueCount; t++) {
        deleteIfExists(entry.getCleanFile(t));
        deleteIfExists(entry.getDirtyFile(t));
      }
      i.remove();
    }
  }
}
```
Comment:
```
Computes the initial size and collects garbage as a part of opening the cache. Dirty entries are assumed to be inconsistent and will be deleted.
```
---
id: 263

Code snippet:
```
public boolean hasAdminData() throws ADSContextException {
  DN[] dns={getAdministratorContainerDN(),getAllServerGroupDN(),getServerContainerDN(),getInstanceKeysContainerDN(),getSecretKeysContainerDN()};
  boolean hasAdminData=true;
  for (int i=0; i < dns.length && hasAdminData; i++) {
    hasAdminData=isExistingEntry(dns[i]);
  }
  return hasAdminData;
}
```
Comment:
```
Returns <CODE>true</CODE> if the server contains Administration Data and <CODE>false</CODE> otherwise.
```
---
id: 264

Code snippet:
```
private void publishUpdateMessages(String testName,ReplicaId replicaId,boolean checkLastCookie,ReplicationMsg... messages) throws Exception {
  ReplicationBroker broker=enableReplication(replicaId);
  String cookie=\"\";
  for (  ReplicationMsg msg : messages) {
    if (msg instanceof UpdateMsg) {
      final UpdateMsg updateMsg=(UpdateMsg)msg;
      assertThat(updateMsg.getCSN().getServerId()).isEqualTo(replicaId.getServerId());
      debugInfo(testName,\" publishes \" + updateMsg.getCSN());
    }
    broker.publish(msg);
    if (checkLastCookie) {
      cookie=assertLastCookieDifferentThanLastValue(cookie);
    }
  }
}
```
Comment:
```
This method is called by the database.
```
---
id: 265

Code snippet:
```
public String displayStructureAsXML(){
  return \"\";
}
```
Comment:
```
Returns a string representation of this object.
```
---
id: 266

Code snippet:
```
public com.sun.identity.wsfederation.jaxb.entityconfig.BaseConfigType createBaseConfigType() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.wsfederation.jaxb.entityconfig.impl.BaseConfigTypeImpl();
}
```
Comment:
```
Create an instance of BaseConfigType
```
---
id: 267

Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  NodeList elementList;
  Node nameNode;
  CharacterData child;
  String badString;
  doc=(Document)load(\"staff\",false);
  elementList=doc.getElementsByTagName(\"address\");
  nameNode=elementList.item(0);
  child=(CharacterData)nameNode.getFirstChild();
{
    boolean success=false;
    try {
      badString=child.substringData(40,3);
    }
 catch (    DOMException ex) {
      success=(ex.code == DOMException.INDEX_SIZE_ERR);
    }
    assertTrue(\"throw_INDEX_SIZE_ERR\",success);
  }
}
```
Comment:
```
Runs the test case.
```
---
id: 268

Code snippet:
```
public void append_to(PlaLineIntAlist dest,int src_pos){
  int poly_len=size();
  for (int index=src_pos; index < poly_len; index++)   dest.add(get(index));
}
```
Comment:
```
Append to dest the remaining lines starting from pos If src_pos is zero and dest is empty this actually copy the list
```
---
id: 269

Code snippet:
```
private MetadataBlockDataPicture createMetadataBlockDataPicture(Artwork artwork) throws FieldDataInvalidException {
  if (artwork.isLinked()) {
    return new MetadataBlockDataPicture(Utils.getDefaultBytes(artwork.getImageUrl(),TextEncoding.CHARSET_ISO_8859_1),artwork.getPictureType(),MetadataBlockDataPicture.IMAGE_IS_URL,\"\",0,0,0,0);
  }
 else {
    if (!artwork.setImageFromData()) {
      throw new FieldDataInvalidException(\"Unable to create MetadataBlockDataPicture from buffered\");
    }
    return new MetadataBlockDataPicture(artwork.getBinaryData(),artwork.getPictureType(),artwork.getMimeType(),artwork.getDescription(),artwork.getWidth(),artwork.getHeight(),0,0);
  }
}
```
Comment:
```
Creates a new block.
```
---
id: 270

Code snippet:
```
public GroupMBean() throws MBeanException, RuntimeOperationsException {
  super();
}
```
Comment:
```
Construct a <code>ModelMBean</code> with default <code>ModelMBeanInfo</code> information.
```
---
id: 271

Code snippet:
```
public IvParameterSpec(byte[] iv,int offset,int byteCount){
  if ((iv == null) || (iv.length - offset < byteCount)) {
    throw new IllegalArgumentException();
  }
  Arrays.checkOffsetAndCount(iv.length,offset,byteCount);
  this.iv=new byte[byteCount];
  System.arraycopy(iv,offset,this.iv,0,byteCount);
}
```
Comment:
```
Creates a new byte array.
```
---
id: 272

Code snippet:
```
@NonNull public static Interpolator clip(Interpolator interpolator,float start,float end){
  return new ClipInterpolator(interpolator,start,end);
}
```
Comment:
```
Calculates the distance between two points
```
---
id: 273

Code snippet:
```
public PartOfSetValue(String value){
  this.rawText=value;
  initFromValue(value);
}
```
Comment:
```
When constructing from data
```
---
id: 274

Code snippet:
```
ResourceIndexEntry findClosestMatch(ServiceType resourceType,String resourceName){
  ResourceIndexEntry resourceIndexEntry=null;
  ResourceMatch rm=resourceType.compare(resourceName,this.resourceName,false);
  if (rm.equals(ResourceMatch.EXACT_MATCH) || rm.equals(ResourceMatch.SUB_RESOURCE_MATCH)) {
    resourceIndexEntry=this;
  }
 else   if (rm.equals(ResourceMatch.SUPER_RESOURCE_MATCH)) {
    Iterator iter=childEntries.iterator();
    boolean processed=false;
    while ((!processed) && (iter.hasNext())) {
      ResourceIndexEntry rie=(ResourceIndexEntry)iter.next();
      resourceIndexEntry=rie.findClosestMatch(resourceType,resourceName);
      if (resourceIndexEntry != null) {
        processed=true;
      }
    }
    if (resourceIndexEntry == null) {
      resourceIndexEntry=this;
    }
  }
  return resourceIndexEntry;
}
```
Comment:
```
Returns the index of the first occurrence of the specified element, or -1 if no match was found.
```
---
id: 275

Code snippet:
```
public void paintToolBarContentBackground(SynthContext context,Graphics g,int x,int y,int w,int h,int orientation){
  paintBackground(context,g,x,y,w,h,orientation);
}
```
Comment:
```
Paints the background of a slider.
```
---
id: 276

Code snippet:
```
private void writeObject(ObjectOutputStream s) throws IOException {
  s.defaultWriteObject();
  if (getUIClassID().equals(uiClassID)) {
    byte count=JComponent.getWriteObjCounter(this);
    JComponent.setWriteObjCounter(this,--count);
    if (count == 0 && ui != null) {
      ui.installUI(this);
    }
  }
}
```
Comment:
```
See <code>readObject</code> and <code>writeObject</code> in <code>JComponent</code> for more information about serialization in Swing.
```
---
id: 277

Code snippet:
```
public int size(){
  return getArray().length;
}
```
Comment:
```
Returns the number of elements in this list.
```
---
id: 278

Code snippet:
```
@Override public int hashCode(){
  int hash=((time.toSecondOfDay() + (timeEndOfDay ? 1 : 0)) << 15) + (month.ordinal() << 11) + ((dom + 32) << 5)+ ((dow == null ? 7 : dow.ordinal()) << 2)+ (timeDefinition.ordinal());
  return hash ^ standardOffset.hashCode() ^ offsetBefore.hashCode()^ offsetAfter.hashCode();
}
```
Comment:
```
Returns a hash code for this instance.
```
---
id: 279

Code snippet:
```
public ValidationException(Throwable exception){
  this(null,null,exception);
}
```
Comment:
```
Constructs a new exception with the specified detail message, cause, and bean for JAX-WS exception serialization.
```
---
id: 280

Code snippet:
```
private static void verifySimpleXMLName(String name) throws XMPException {
  if (!Utils.isXMLName(name)) {
    throw new XMPException(\"Bad XML name\",XMPError.BADXPATH);
  }
}
```
Comment:
```
Ensures the truth of an expression involving the state of the calling instance, but not involving any parameters to the calling method.
```
---
id: 281

Code snippet:
```
public void test_removeAt_siftUp(){
  PriorityQueue<Integer> q=new PriorityQueue<Integer>();
  for (  int i : new int[]{0,3,1,4,5,6,2}) {
    q.add(i);
  }
  q.remove(4);
  for (  int i : new int[]{0,1,2,3,5,6}) {
    assertEquals(i,(int)q.poll());
  }
  assertNull(q.poll());
}
```
Comment:
```
removeAt(.) must sometimes perform siftUp(.).
```
---
id: 282

Code snippet:
```
public ContextResourceLinkMBean() throws MBeanException, RuntimeOperationsException {
  super();
}
```
Comment:
```
Construct a <code>ModelMBean</code> with default <code>ModelMBeanInfo</code> information.
```
---
id: 283

Code snippet:
```
public void beginMonitoringOf(final InetAddress inetAddress,final int inode){
  final long socketIdentifier=fromInet4AddressAndInode(inetAddress,inode);
  candidateSockets.beginMonitoringSocketIdentifier(new InetSocketAddress(inetAddress,0),socketIdentifier);
}
```
Comment:
```
Starts the handshake.
```
---
id: 284

Code snippet:
```
public static String encode(String s){
  String ret=null;
  try {
    ret=encode(s,UTF_8);
  }
 catch (  UnsupportedEncodingException e) {
  }
  return ret;
}
```
Comment:
```
Translates a string into <code>application/x-www-form-urlencoded</code> format using the UTF-8 encoding scheme. The <a href=\"http://www.w3.org/TR/html40/appendix/notes.html#non-ascii-chars\"> World Wide Web Consortium Recommendation</a> states that UTF-8 should be used to ensure compatibilities.
```
---
id: 285

Code snippet:
```
public void handleBtnPreviousRequest(RequestInvocationEvent event){
  String orgDN=(String)getPageSessionAttribute(ORG_DN);
  String value=(String)getPageSessionAttribute(USER_ATTR_VALUE);
  String locale=(String)getPageSessionAttribute(URL_LOCALE);
  String initialOrgDN=(String)getPageSessionAttribute(INITIAL_ORG_DN);
  PWResetUserValidationViewBean vb=(PWResetUserValidationViewBean)getViewBean(PWResetUserValidationViewBean.class);
  vb.setPageSessionAttribute(ORG_DN,initialOrgDN);
  vb.setPageSessionAttribute(USER_ATTR_VALUE,value);
  vb.setPageSessionAttribute(URL_LOCALE,locale);
  String orgDNFlag=(String)getPageSessionAttribute(ORG_DN_FLAG);
  if (orgDNFlag != null && orgDNFlag.equals(STRING_TRUE)) {
    vb.setPageSessionAttribute(ORG_DN_FLAG,STRING_TRUE);
  }
  vb.forwardTo(getRequestContext());
}
```
Comment:
```
Handles the event.
```
---
id: 286

Code snippet:
```
public void removeUpdate(DocumentEvent changes,Shape a,ViewFactory f){
  updateDamage(changes,a,f);
}
```
Comment:
```
Remove a listener from the list of listeners.
```
---
id: 287

Code snippet:
```
public DataStoreProviderException(String message){
  super(message);
}
```
Comment:
```
Constructs a new exception with the specified detail message. The cause is not initialized.
```
---
id: 288

Code snippet:
```
public synchronized BukkitTask runTaskLaterAsynchronously(Plugin plugin,long delay) throws IllegalArgumentException, IllegalStateException {
  checkState();
  return setupId(Bukkit.getScheduler().runTaskLaterAsynchronously(plugin,(Runnable)this,delay));
}
```
Comment:
```
<b>Asynchronous tasks should never access any API in Bukkit. Great care should be taken to assure the thread-safety of asynchronous tasks.</b> <p> Schedules this to run asynchronously after the specified number of server ticks.
```
---
id: 289

Code snippet:
```
private final static void println(String msg){
  System.out.println(msg);
}
```
Comment:
```
print/println stuff...
```
---
id: 290

Code snippet:
```
public void disableVertexAttribute(String name){
  int location=fetchAttributeLocation(name);
  if (location == -1)   return;
  GLES20.glDisableVertexAttribArray(location);
}
```
Comment:
```
Disables the vertex attribute with the given name
```
---
id: 291

Code snippet:
```
public Observable<Void> removeJobObservable(long id){
  io.vertx.rx.java.ObservableFuture<Void> handler=io.vertx.rx.java.RxHelper.observableFuture();
  removeJob(id,handler.toHandler());
  return handler;
}
```
Comment:
```
Removes a node from the group.
```
---
id: 292

Code snippet:
```
public boolean isCompressionLossless(){
  if (getCompressionMode() != MODE_EXPLICIT) {
    throw new IllegalStateException(\"Compression mode not MODE_EXPLICIT!\");
  }
  return false;
}
```
Comment:
```
Returns <code>false</code> since the JPEG plug-in only supports lossy compression.
```
---
id: 293

Code snippet:
```
public void testCFII_ServerStartLater_Block() throws Exception {
  ensureServerClosed();
  assertTrue(this.channel1.isBlocking());
  statusNotConnected_NotPending();
  try {
    this.channel1.connect(localAddr1);
    fail(\"Should throw a ConnectException here.\");
  }
 catch (  ConnectException e) {
  }
  statusChannelClosed();
  ensureServerOpen();
  try {
    this.channel1.finishConnect();
    fail(\"Should throw a ClosedChannelException here.\");
  }
 catch (  ClosedChannelException e) {
  }
}
```
Comment:
```
Test method for \'DatagramChannelImpl.receive(ByteBuffer)\'
```
---
id: 294

Code snippet:
```
private static int findAnyZero(float[] a,int low,int high){
  while (true) {
    int middle=(low + high) >>> 1;
    float middleValue=a[middle];
    if (middleValue < 0.0f) {
      low=middle + 1;
    }
 else     if (middleValue > 0.0f) {
      high=middle - 1;
    }
 else {
      return middle;
    }
  }
}
```
Comment:
```
Returns the index of some zero element in the specified range via binary search. The range is assumed to be sorted, and must contain at least one zero.
```
---
id: 295

Code snippet:
```
@SuppressWarnings(\"unused\") public static void translatePoint(PointF point,float offsetX,float offsetY,float angle){
  ScFeature.translatePoint(point,offsetX,angle);
  ScFeature.translatePoint(point,offsetY,angle + 90.0f);
}
```
Comment:
```
Translates a point from a pair of points to the range axis.
```
---
id: 296

Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(hc_nodeparentnodenull.class,args);
}
```
Comment:
```
Runs this test from the command line.
```
---
id: 297

Code snippet:
```
public long seed(){
  return seed;
}
```
Comment:
```
Returns the number of bytes currently being used to store the values in this cache. This may be greater than the max size if a background deletion is pending.
```
---
id: 298

Code snippet:
```
public static void evaluateBundleValues(ResourceBundle bundle,Properties lookupProp){
  Enumeration propNames=bundle.getKeys();
  while (propNames.hasMoreElements()) {
    String name=(String)propNames.nextElement();
    String value=(String)SetupUtils.evaluatePropertiesValue(bundle.getString(name),lookupProp);
    if (value != null) {
      lookupProp.setProperty(name,value);
    }
  }
}
```
Comment:
```
Lookups and set the resource bundle variables to the Properties
```
---
id: 299

Code snippet:
```
public boolean isSticky(){
  return this.getItemType() == Material.PISTON_STICKY_BASE;
}
```
Comment:
```
Gets the value of the isScorable property.
```
---
