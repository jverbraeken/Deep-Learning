id: 300

Code snippet:
```
public void shutdown(){
synchronized (msgQueue) {
    msgQueue.clear();
    msgQueue.notify();
    msgQueue.notifyAll();
  }
  DirectoryServer.deregisterMonitorProvider(this);
}
```
Comment:
```
Shutdown this handler.
```
---
id: 301

Code snippet:
```
public static StartTLSExtendedRequest newStartTLSExtendedRequest(final SSLContext sslContext){
  return new StartTLSExtendedRequestImpl(sslContext);
}
```
Comment:
```
Creates a new start tls extended request which will use the provided ssl context.
```
---
id: 302

Code snippet:
```
public void write(int b){
  try {
synchronized (this) {
      ensureOpen();
      out.write(b);
      if ((b == \'
\') && autoFlush)       out.flush();
    }
  }
 catch (  InterruptedIOException x) {
    Thread.currentThread().interrupt();
  }
catch (  IOException x) {
    trouble=true;
  }
}
```
Comment:
```
Description of the method.
```
---
id: 303

Code snippet:
```
public void paintSliderThumbBackground(SynthContext context,Graphics g,int x,int y,int w,int h,int orientation){
}
```
Comment:
```
Paints the background of the thumb of a slider.
```
---
id: 304

Code snippet:
```
public void testGetInstanceStringString03() throws IllegalArgumentException, NoSuchAlgorithmException, NoSuchProviderException {
  if (!DEFSupported) {
    fail(NotSupportMsg);
    return;
  }
  KeyAgreement keyA;
  for (int i=0; i < validValues.length; i++) {
    keyA=KeyAgreement.getInstance(validValues[i],defaultProviderName);
    assertEquals(\"Incorrect algorithm\",keyA.getAlgorithm(),validValues[i]);
    assertEquals(\"Incorrect provider\",keyA.getProvider().getName(),defaultProviderName);
  }
}
```
Comment:
```
Test for <code>getinstance(string algorithm, string provider)</code> method assertion: throws nullpointerexception when algorithm is null; throws nosuchalgorithmexception when algorithm is not correct;.
```
---
id: 305

Code snippet:
```
public static boolean hasDescriptor(LocalizableMessage msg,LocalizableMessageDescriptor.Arg7<?,?,?,?,?,?,?> desc){
  return msg.ordinal() == desc.ordinal() && msg.resourceName().equals(desc.resourceName());
}
```
Comment:
```
Test if the provided message corresponds to the provided descriptor.
```
---
id: 306

Code snippet:
```
public PrincipalHolder(Principal initial){
  value=initial;
}
```
Comment:
```
Constructs a new <code>principalholder</code> object with its <code>value</code> field initialized to the given <code>principal</code> object.
```
---
id: 307

Code snippet:
```
public static boolean expectResponseEntityBody(String requestMethod){
  return !StringUtils.equals(requestMethod,HEAD);
}
```
Comment:
```
Returns true if the specified <code>entity</code> is <code>null</code>.
```
---
id: 308

Code snippet:
```
public MetadataDescriptor createCopy(){
  final MetadataDescriptor result=new MetadataDescriptor(this.containerType,this.name,this.descriptorType,this.streamNumber,this.languageIndex);
  result.content=getRawData();
  return result;
}
```
Comment:
```
This method creates a copy of the current object. <br> all data will be copied, too. <br>.
```
---
id: 309

Code snippet:
```
public ForwardRelationshipValidator(RelationshipProvider relationshipProvider){
  super(relationshipProvider);
}
```
Comment:
```
Creates a new validator.
```
---
id: 310

Code snippet:
```
public static void write(OutputStream out,NSObject root) throws IOException {
  int minVersion=getMinimumRequiredVersion(root);
  if (minVersion > VERSION_00) {
    String versionString=((minVersion == VERSION_10) ? \"v1.0\" : ((minVersion == VERSION_15) ? \"v1.5\" : ((minVersion == VERSION_20) ? \"v2.0\" : \"v0.0\")));
    throw new IOException(\"The given property list structure cannot be saved. \" + \"The required version of the binary format (\" + versionString + \") is not yet supported.\");
  }
  BinaryPropertyListWriter w=new BinaryPropertyListWriter(out,minVersion);
  w.write(root);
}
```
Comment:
```
Writes a binary plist serialization of the given object as the root.
```
---
id: 311

Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(documentimportnode01.class,args);
}
```
Comment:
```
Runs this test from the command line.
```
---
id: 312

Code snippet:
```
public static TextHitInfo trailing(int charIndex){
  return new TextHitInfo(charIndex,false);
}
```
Comment:
```
Returns the position of the given text.
```
---
id: 313

Code snippet:
```
@Override public String toString(){
  return mediaType;
}
```
Comment:
```
Returns the encoded media type, like \"text/plain; charset=utf-8\", appropriate for use in a content-type header.
```
---
id: 314

Code snippet:
```
public JDialog createDialog(Component parentComponent,String title) throws HeadlessException {
  int style=styleFromMessageType(getMessageType());
  return createDialog(parentComponent,title,style);
}
```
Comment:
```
Creates and returns a new <code>jdialog</code> wrapping <code>this</code> centered on the <code>parentcomponent</code> in the <code>parentcomponent</code>\'s frame. <code>title</code> is the title of the returned dialog. the returned <code>jdialog</code> will not be resizable by the user, however programs can invoke <code>setresizable</code> on the <code>jdialog</code> instance to change this property. the returned <code>jdialog</code> will be set up such that once it is closed, or the user clicks on one of the buttons, the optionpane\'s value property will be set accordingly and the dialog will be closed. each time the dialog is made visible, it will reset the option pane\'s value property to <code>joptionpane.uninitialized_value</code> to ensure the user\'s subsequent action closes the dialog properly.
```
---
id: 315

Code snippet:
```
public Hashtable<String,Object> toHash(){
  final Hashtable<String,Object> values=new Hashtable();
  for (int i=0; i < this.columnsValues.size(); i++) {
    final JKTableColumnValue value=this.columnsValues.get(i);
    values.put(getColumn(i).getName(),value);
  }
  return values;
}
```
Comment:
```
To hash.
```
---
id: 316

Code snippet:
```
public static String formatSeconds(Object obj){
  long time=-1L;
  if (obj instanceof Long) {
    time=((Long)obj).longValue();
  }
 else   if (obj instanceof Integer) {
    time=((Integer)obj).intValue();
  }
  return (time + \" s\");
}
```
Comment:
```
Formats the given time (given in seconds) as a string.
```
---
id: 317

Code snippet:
```
void resetHeaderBuffer(){
  pos=0;
}
```
Comment:
```
Reset the buffer.
```
---
id: 318

Code snippet:
```
public boolean isRealmSubject(String subjectName) throws NameNotFoundException {
  if (!users.containsKey(subjectName)) {
    String[] objs={subjectName};
    throw (new NameNotFoundException(ResBundleUtils.rbName,\"name_not_present\",objs,subjectName,PolicyException.USER_COLLECTION));
  }
 else {
    return ((QualifiedSubject)users.get(subjectName)).isRealmSubject();
  }
}
```
Comment:
```
Checks if the subject is a reference to a <code>subject</code> defined at the realm.
```
---
id: 319

Code snippet:
```
public void addSessionPartner(SAML2SessionPartner sessionPartner){
  Iterator i=sessionPartners.iterator();
  while (i.hasNext()) {
    if (((SAML2SessionPartner)i.next()).equals(sessionPartner)) {
      return;
    }
  }
  sessionPartners.add(sessionPartner);
}
```
Comment:
```
Add a session to this session.
```
---
id: 320

Code snippet:
```
public final void testDEFAULTmdName(){
  assertEquals(\"SHA-1\",PSSParameterSpec.DEFAULT.getDigestAlgorithm());
}
```
Comment:
```
Test for <code>default</code> field<br> assertion: default message digest algorithm name is \"sha-1\".
```
---
id: 321

Code snippet:
```
@Override public void toString(StringBuilder buffer){
  buffer.append(\"JmxClientConnection(connID=\");
  buffer.append(connectionID);
  buffer.append(\", authDN=\\"\");
  buffer.append(getAuthenticationInfo().getAuthenticationDN());
  buffer.append(\"\\")\");
}
```
Comment:
```
This method gets called when a connection is closed.
```
---
id: 322

Code snippet:
```
private DateEditor(JSpinner spinner,DateFormat format){
  super(spinner);
  if (!(spinner.getModel() instanceof SpinnerDateModel)) {
    throw new IllegalArgumentException(\"model not a SpinnerDateModel\");
  }
  SpinnerDateModel model=(SpinnerDateModel)spinner.getModel();
  DateFormatter formatter=new DateEditorFormatter(model,format);
  DefaultFormatterFactory factory=new DefaultFormatterFactory(formatter);
  JFormattedTextField ftf=getTextField();
  ftf.setEditable(true);
  ftf.setFormatterFactory(factory);
  try {
    String maxString=formatter.valueToString(model.getStart());
    String minString=formatter.valueToString(model.getEnd());
    ftf.setColumns(Math.max(maxString.length(),minString.length()));
  }
 catch (  ParseException e) {
  }
}
```
Comment:
```
Construct a <code>jspinner</code> editor that supports displaying and editing the value of a <code>spinnerdatemodel</code> with a <code>jformattedtextfield</code>. <code>this</code> <code>dateeditor</code> becomes both a <code>changelistener</code> on the spinner and a <code>propertychangelistener</code> on the new <code>jformattedtextfield</code>.
```
---
id: 323

Code snippet:
```
public com.sun.identity.wsfederation.jaxb.wsspolicy.XPathFilter20Element createXPathFilter20Element() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.wsfederation.jaxb.wsspolicy.impl.XPathFilter20ElementImpl();
}
```
Comment:
```
Create an instance of xpathfilter20element.
```
---
id: 324

Code snippet:
```
public static String convertFromUriEncoding(final String fileName,final IConfiguration configuration){
  try {
    return new String(fileName.getBytes(configuration.getUriEncoding()),\"UTF-8\");
  }
 catch (  UnsupportedEncodingException e) {
    return fileName;
  }
}
```
Comment:
```
Converts filename to connector encoding.
```
---
id: 325

Code snippet:
```
public void add(Permission permission){
  if (isReadOnly())   throw new SecurityException(\"attempt to add a Permission to a readonly Permissions object\");
  PermissionCollection pc;
synchronized (this) {
    pc=getPermissionCollection(permission,true);
    pc.add(permission);
  }
  if (permission instanceof AllPermission) {
    allPermission=pc;
  }
  if (permission instanceof UnresolvedPermission) {
    hasUnresolved=true;
  }
}
```
Comment:
```
Adds a permission to the list of permissions.
```
---
id: 326

Code snippet:
```
public String compress(String imageUri){
  return compressImage(imageUri);
}
```
Comment:
```
Compresses the image at the specified uri string and and return the filepath of the compressed image.
```
---
id: 327

Code snippet:
```
public boolean isValid(){
  return messenger.isRegistrationValid(this);
}
```
Comment:
```
Returns true if this view is valid.
```
---
id: 328

Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  NodeList elementList;
  Node nameNode;
  CharacterData child;
  String childValue;
  int childLength;
  doc=(Document)load(\"staff\",true);
  elementList=doc.getElementsByTagName(\"name\");
  nameNode=elementList.item(0);
  child=(CharacterData)nameNode.getFirstChild();
  child.appendData(\", Esquire\");
  childValue=child.getData();
  childLength=childValue.length();
  assertEquals(\"characterdataAppendDataAssert\",24,childLength);
}
```
Comment:
```
Runs the test case.
```
---
id: 329

Code snippet:
```
public JCheckBoxMenuItem(String text,boolean b){
  this(text,null,b);
}
```
Comment:
```
Creates a new instance.
```
---
id: 330

Code snippet:
```
@Override public void onLoginFailure(Map requestParamsMap,HttpServletRequest request,HttpServletResponse response){
}
```
Comment:
```
Called when the user is authenticated.
```
---
id: 331

Code snippet:
```
boolean isValidMask(){
  return validMask;
}
```
Comment:
```
Returns true if the current mask is valid.
```
---
id: 332

Code snippet:
```
public final boolean sameNodeAs(Node other){
  if (!(other instanceof DTMNodeProxy))   return false;
  DTMNodeProxy that=(DTMNodeProxy)other;
  return this.dtm == that.dtm && this.node == that.node;
}
```
Comment:
```
Future dom: test node identity, in lieu of node==node.
```
---
id: 333

Code snippet:
```
public boolean isClosed(){
  return state == STATE_CLOSED;
}
```
Comment:
```
Returns true if this connection is closed.
```
---
id: 334

Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  DocumentType docType;
  NamedNodeMap notations;
  Node notationNode;
  String notationName;
  doc=(Document)load(\"staff\",false);
  docType=doc.getDoctype();
  assertNotNull(\"docTypeNotNull\",docType);
  notations=docType.getNotations();
  assertNotNull(\"notationsNotNull\",notations);
  notationNode=notations.getNamedItem(\"notation1\");
  assertNotNull(\"notationNotNull\",notationNode);
  notationName=notationNode.getNodeName();
  assertEquals(\"nodeName\",\"notation1\",notationName);
}
```
Comment:
```
Runs the test case.
```
---
id: 335

Code snippet:
```
private void sendModeMessage(){
  currWSstateLock.lock();
  currWSstate=WSstate.WS_MODE_SWITCHED;
  currWSstateLock.unlock();
  String instrumentString=getInstrumentString(instrumentList);
  String msg=\"{\\"a\\": \\"mode\\", \\"v\\": [\\"\" + ZStreamingConfig.getStreamingQuoteMode() + \"\\", [\"+ instrumentString+ \"]]}\";
  System.out.println(\"WebsocketThread.sendModeMessage(): WS mode msg: \" + msg);
  clientEndPoint.sendMessage(msg);
  fireDataMissTimerOnWSsubscribe();
}
```
Comment:
```
Sendmodemessage - private method to send mode message for the instruments.
```
---
id: 336

Code snippet:
```
public FSPreLoginException(Throwable t,String msg){
  super(t,msg);
}
```
Comment:
```
Constructs a new exception with the specified detail message, cause, and bean for jax-ws exception serialization.
```
---
id: 337

Code snippet:
```
static void createDirectory(final String directory) throws IOException {
  File dir=new File(directory);
  if (!dir.exists()) {
    if (!dir.mkdirs()) {
      throw new IOException(\"Failed to create directory: \" + directory);
    }
  }
}
```
Comment:
```
Creates a directory unless it already exists.
```
---
id: 338

Code snippet:
```
public KeywordMap(boolean ignoreCase,int mapLength){
  this.mapLength=mapLength;
  this.ignoreCase=ignoreCase;
  map=new Keyword[mapLength];
}
```
Comment:
```
Creates a new <code>keywordmap</code>.
```
---
id: 339

Code snippet:
```
public void addOperand(PdfVisibilityExpression expression){
  getPdfObject().add(expression.getPdfObject());
  getPdfObject().setModified();
}
```
Comment:
```
Adds a new opeand to the current visibility expression.
```
---
id: 340

Code snippet:
```
public String toString(){
  StringBuilder sb=new StringBuilder();
  sb.append(\"StateInfo ID:[\").append(this.id).append(\"], \");
  sb.append(\"Protocol:[\").append(this.protocol).append(\"], \");
  sb.append(\"URL:[\").append(((this.url == null) ? \"null\" : this.url.toString()));
  sb.append(\"], \");
  sb.append(\"Address:[\");
  if (this.address == null) {
    sb.append(\"null], \");
  }
 else {
    sb.append(this.address.toString()).append(\"], Unresolved:[\");
    sb.append(this.address.isUnresolved()).append(\"], \");
  }
  sb.append(\"Local:[\").append(this.isLocal).append(\"], \");
  sb.append(\"Up:[\").append(this.isUp).append(\"].
\");
  return sb.toString();
}
```
Comment:
```
Tostring methode: creates a string representation of the object.
```
---
id: 341

Code snippet:
```
private boolean isClosed(){
  return buf == null;
}
```
Comment:
```
Returns true if this stream is closed.
```
---
id: 342

Code snippet:
```
public JPanel(){
  this(true);
}
```
Comment:
```
Creates a new panel.
```
---
id: 343

Code snippet:
```
public synchronized void readRequest(){
  if (currentWriters == 0 && writerLocks.size() == 0) {
    ++currentReaders;
  }
 else {
    ++queuedReaders;
    try {
      wait();
    }
 catch (    InterruptedException e) {
    }
  }
}
```
Comment:
```
Writes the request to the pipeline.
```
---
id: 344

Code snippet:
```
public void store(SSOToken token) throws SMSException, SSOException {
}
```
Comment:
```
Save changed to persistent store.
```
---
id: 345

Code snippet:
```
public int readWord() throws IOException {
  length+=2;
  int k1=in.read();
  if (k1 < 0)   return 0;
  return (k1 + (in.read() << 8)) & 0xffff;
}
```
Comment:
```
Reads a word.
```
---
id: 346

Code snippet:
```
public int stack_depth(){
  return max_stack_level;
}
```
Comment:
```
Returns the maximum recursion depth for shoving the obstacle traces.
```
---
id: 347

Code snippet:
```
public void testIntValueNegative1(){
  byte aBytes[]={12,56,100,-2,-76,-128,45,91,3};
  int sign=-1;
  int resInt=2144511229;
  int aNumber=new BigInteger(sign,aBytes).intValue();
  assertTrue(aNumber == resInt);
}
```
Comment:
```
Convert a negative biginteger to an integer value. the low digit is negative.
```
---
id: 348

Code snippet:
```
public JarEntry(String name){
  super(name);
}
```
Comment:
```
Creates a new entry.
```
---
id: 349

Code snippet:
```
public DoubleHolder(double initial){
  value=initial;
}
```
Comment:
```
Creates a new instance.
```
---
id: 350

Code snippet:
```
public void stopHandler(){
  if (logger.isTraceEnabled()) {
    debugInfo(\"stop\");
  }
  DirectoryServer.deregisterMonitorProvider(this);
}
```
Comment:
```
Stops the server.
```
---
id: 351

Code snippet:
```
protected void calcScore(){
  if ((m_namespace == null) && (m_name == null))   m_score=SCORE_NODETEST;
 else   if (((m_namespace == WILD) || (m_namespace == null)) && (m_name == WILD))   m_score=SCORE_NODETEST;
 else   if ((m_namespace != WILD) && (m_name == WILD))   m_score=SCORE_NSWILD;
 else   m_score=SCORE_QNAME;
  m_isTotallyWild=(m_namespace == null && m_name == WILD);
}
```
Comment:
```
Static calc of match score.
```
---
id: 352

Code snippet:
```
public static String addSchemaFileToElementDefinitionIfAbsent(String definition,String schemaFile){
  if (schemaFile != null && !definition.contains(SCHEMA_PROPERTY_FILENAME)) {
    int pos=definition.lastIndexOf(\')\');
    return definition.substring(0,pos).trim() + \" \" + SCHEMA_PROPERTY_FILENAME+ \" \'\"+ schemaFile+ \"\' )\";
  }
  return definition;
}
```
Comment:
```
Adds the provided schema file to the provided schema element definition.
```
---
id: 353

Code snippet:
```
public void postProcess(final HttpResponse response,final HttpProcessor processor,final HttpContext context) throws HttpException, IOException {
  if (response == null) {
    throw new IllegalArgumentException(\"HTTP response may not be null\");
  }
  if (processor == null) {
    throw new IllegalArgumentException(\"HTTP processor may not be null\");
  }
  if (context == null) {
    throw new IllegalArgumentException(\"HTTP context may not be null\");
  }
  processor.process(response,context);
}
```
Comment:
```
Finish a response. this includes post-processing of the response object. it does <i>not</i> read the response entity, if any. it does <i>not</i> allow for immediate re-use of the connection over which the response is coming in.
```
---
id: 354

Code snippet:
```
public void print(double dnum){
  print(String.valueOf(dnum));
}
```
Comment:
```
Prints the string representation of the specified double to the target.
```
---
id: 355

Code snippet:
```
public Map<String,Request> pathToRequest(){
  return pathToRequest;
}
```
Comment:
```
Returns a map from recently-requested paths (like \"/index.html\") to a snapshot of the request data.
```
---
id: 356

Code snippet:
```
public InternalClientConnection(DN userDN) throws DirectoryException {
  this(getAuthInfoForDN(userDN));
}
```
Comment:
```
Creates a new instance.
```
---
id: 357

Code snippet:
```
public long numSubordinates(final DN entryDN,final boolean subtree) throws ConfigException {
  final ConfigLdapResultHandler resultHandler=new ConfigLdapResultHandler();
  final CollectorSearchResultHandler searchHandler=new CollectorSearchResultHandler();
  final SearchScope scope=subtree ? SearchScope.SUBORDINATES : SearchScope.SINGLE_LEVEL;
  final SearchRequest searchRequest=Requests.newSearchRequest(entryDN,scope,Filter.alwaysTrue());
  backend.handleSearch(UNCANCELLABLE_REQUEST_CONTEXT,searchRequest,null,searchHandler,resultHandler);
  if (resultHandler.hasCompletedSuccessfully()) {
    return searchHandler.getEntries().size();
  }
  throw new ConfigException(ERR_UNABLE_TO_RETRIEVE_CHILDREN_OF_CONFIGURATION_ENTRY.get(entryDN),resultHandler.getResultError());
}
```
Comment:
```
Retrieves the number of subordinates for the requested entry.
```
---
id: 358

Code snippet:
```
public EACCredentials(PrivateKey privateKey,Certificate[] chain){
  this.privateKey=privateKey;
  this.chain=chain;
}
```
Comment:
```
Creates a new <code>certpath</code> instance.
```
---
id: 359

Code snippet:
```
public Passport(PassportService service,MRTDTrustStore trustManager,BACKeySpec bacKey) throws CardServiceException, GeneralSecurityException {
  this(service,trustManager,Collections.singletonList(bacKey),false,false);
}
```
Comment:
```
Creates a document by reading it from a service. access control will be bac only.
```
---
id: 360

Code snippet:
```
public boolean offer(E o){
  if (o == null) {
    throw new NullPointerException(\"o == null\");
  }
  growToSize(size + 1);
  elements[size]=o;
  siftUp(size++);
  return true;
}
```
Comment:
```
Inserts the element to the priority queue.
```
---
id: 361

Code snippet:
```
public void characters(char ch[],int start,int length) throws org.xml.sax.SAXException {
  if (!m_shouldProcess)   return;
  XSLTElementProcessor elemProcessor=getCurrentProcessor();
  XSLTElementDef def=elemProcessor.getElemDef();
  if (def.getType() != XSLTElementDef.T_PCDATA)   elemProcessor=def.getProcessorFor(null,\"text()\");
  if (null == elemProcessor) {
    if (!XMLCharacterRecognizer.isWhiteSpace(ch,start,length))     error(XSLMessages.createMessage(XSLTErrorResources.ER_NONWHITESPACE_NOT_ALLOWED_IN_POSITION,null),null);
  }
 else   elemProcessor.characters(this,ch,start,length);
}
```
Comment:
```
Receive notification of character data inside an element.
```
---
id: 362

Code snippet:
```
public ShapeTileOctagon to_octagon(){
  if (rx < lx || uy < ly || lrx < ulx || urx < llx) {
    return ShapeTileOctagon.EMPTY;
  }
  return new ShapeTileOctagon(Math.floor(lx),Math.floor(ly),Math.ceil(rx),Math.ceil(uy),Math.floor(ulx),Math.ceil(lrx),Math.floor(llx),Math.ceil(urx));
}
```
Comment:
```
Returns the y-coordinate of this tile.
```
---
id: 363

Code snippet:
```
static private void printAnnotationArray(String prefix,Annotation[] arr){
  TreeMap<String,Annotation> sorted=new TreeMap<String,Annotation>();
  for (  Annotation a : arr) {
    sorted.put(a.annotationType().getName(),a);
  }
  for (  Annotation a : sorted.values()) {
    System.out.println(prefix + \"  \" + annotationToString(a));
    System.out.println(prefix + \"    \" + a.annotationType());
  }
}
```
Comment:
```
Prints the given annotation.
```
---
id: 364

Code snippet:
```
public boolean is_placed_on_front(){
  return true;
}
```
Comment:
```
Returns <code>true</code>.
```
---
id: 365

Code snippet:
```
public boolean isEmpty(){
  return true;
}
```
Comment:
```
Implements for generaltaskrunnable.
```
---
id: 366

Code snippet:
```
public NamingRequest parseXML(){
  if (document == null) {
    return null;
  }
  Element elem=document.getDocumentElement();
  NamingRequest namingRequest=new NamingRequest();
  String temp=elem.getAttribute(\"vers\");
  if (temp != null) {
    namingRequest.setRequestVersion(temp);
  }
  temp=elem.getAttribute(\"reqid\");
  if (temp != null) {
    namingRequest.setRequestID(temp);
  }
  temp=elem.getAttribute(\"sessid\");
  if ((temp != null) && ((temp.trim()).length() != 0)) {
    namingRequest.setSessionId(temp);
  }
 else {
    namingRequest.setSessionId(null);
  }
  temp=elem.getAttribute(\"preferredNamingURL\");
  if ((temp != null) && ((temp.trim()).length() != 0)) {
    namingRequest.setPreferredNamingURL(temp);
  }
 else {
    namingRequest.setPreferredNamingURL(null);
  }
  return namingRequest;
}
```
Comment:
```
Parses an element from the request.
```
---
id: 367

Code snippet:
```
private void iterateIndex(ReadableTransaction txn) throws StorageRuntimeException, DirectoryException {
  if (verifyDN2ID) {
    iterateDN2ID(txn);
  }
 else   if (verifyID2ChildrenCount) {
    iterateID2ChildrenCount(txn);
  }
 else   if (!attrIndexList.isEmpty()) {
    AttributeIndex attrIndex=attrIndexList.get(0);
    for (    MatchingRuleIndex index : attrIndex.getNameToIndexes().values()) {
      iterateAttrIndex(txn,index);
    }
  }
 else   if (!vlvIndexList.isEmpty()) {
    iterateVLVIndex(txn,vlvIndexList.get(0),true);
  }
}
```
Comment:
```
Iterate through the entries in an index to perform a check for index cleanliness. for each id in the index we check that the entry it refers to does indeed contain the expected value.
```
---
id: 368

Code snippet:
```
public static Request parseXML(String xml) throws SAMLException {
  Document doc=XMLUtils.toDOMDocument(xml,SAMLUtils.debug);
  Element root=doc.getDocumentElement();
  return new Request(root);
}
```
Comment:
```
Parses an element of the specified type.
```
---
id: 369

Code snippet:
```
public MoveNextLineAndShowTextOperator(TextMoveNextLineOperator textMoveNextLine,ShowTextOperator showText){
  this.textMoveNextLine=textMoveNextLine;
  this.showText=showText;
}
```
Comment:
```
Creates a new instance.
```
---
id: 370

Code snippet:
```
public String toXMLString() throws XACMLException {
  return toXMLString(true,false);
}
```
Comment:
```
Returns a string representation of this object.
```
---
id: 371

Code snippet:
```
public boolean show(Container c,int x,int y,int w,int h){
  return false;
}
```
Comment:
```
Shows a region of a previously rendered component. this will return true if successful, false otherwise. the default implementation returns false.
```
---
id: 372

Code snippet:
```
public void removeFromTag(){
  parameters.delete(ParameterNames.FROM_TAG);
}
```
Comment:
```
Remove tag.
```
---
id: 373

Code snippet:
```
private void readObject(ObjectInputStream s) throws ClassNotFoundException, IOException {
  s.defaultReadObject();
  myMimeType=new MimeType((String)s.readObject());
}
```
Comment:
```
Adds semantic checks to the default deserialization method. this method must have the standard signature for a readobject method, and the body of the method must begin with \"s.defaultreadobject();\". other than that, any semantic checks can be specified and do not need to stay the same from version to version. a readobject method of this form may be added to any class, even if tetrad sessions were previously saved out using a version of the class that didn\'t include it. (that\'s what the \"s.defaultreadobject();\" is for. see j. bloch, effective java, for help.
```
---
id: 374

Code snippet:
```
public int next(){
  final int node=_currentNode;
  if (node != NULL) {
    _currentNode=getNextAttributeIdentity(node);
    return returnNode(makeNodeHandle(node));
  }
  return NULL;
}
```
Comment:
```
Get the next node in the iteration.
```
---
id: 375

Code snippet:
```
@Override public String toString(){
  return currencyCode;
}
```
Comment:
```
Returns this currency\'s iso 4217 currency code.
```
---
id: 376

Code snippet:
```
@AfterClass public static void cleanupClass(){
  try {
    Misc.deleteDirectorySimple(scenario.getRepositoryLocation());
  }
 catch (  Exception ignore) {
    System.err.println(\"cannot remove \" + scenario.getRepositoryLocation());
  }
}
```
Comment:
```
Cleanup the whole junit scenario ; deletes the created git repository.
```
---
id: 377

Code snippet:
```
public JobMessageFromOperator(String message,Locale locale){
  super(message,locale);
}
```
Comment:
```
Constructs a new exception with the specified detail message. the cause is not initialized.
```
---
id: 378

Code snippet:
```
public static SearchRequest newSearchRequest(final DN name,final SearchScope scope,final Filter filter,final String... attributeDescriptions){
  Reject.ifNull(name,scope,filter);
  final SearchRequest request=new SearchRequestImpl(name,scope,filter);
  for (  final String attributeDescription : attributeDescriptions) {
    request.addAttribute(attributeDescription);
  }
  return request;
}
```
Comment:
```
Creates a new search request using the provided distinguished name, scope, and filter.
```
---
id: 379

Code snippet:
```
@Override public Foo fetchByField2_Last(boolean field2,OrderByComparator<Foo> orderByComparator){
  int count=countByField2(field2);
  if (count == 0) {
    return null;
  }
  List<Foo> list=findByField2(field2,count - 1,count,orderByComparator);
  if (!list.isEmpty()) {
    return list.get(0);
  }
  return null;
}
```
Comment:
```
Returns the last foo in the ordered set where field2 = &#63;.
```
---
id: 380

Code snippet:
```
public boolean hasPredicates(){
  return !CollectionUtils.isEmpty(predicates);
}
```
Comment:
```
Returns <tt>true</tt> if this set contains no elements.
```
---
id: 381

Code snippet:
```
public List<Attribute> toAttributeList() throws IllegalStateException {
  return CollectionUtils.newArrayList(toAttribute());
}
```
Comment:
```
Returns a list with a single attribute representing the content of this attribute builder. <p> for efficiency purposes this method resets the content of this attribute builder so that it no longer contains any options or values and its attribute type is <code>null</code>.
```
---
id: 382

Code snippet:
```
public NumberEditor(JSpinner spinner){
  this(spinner,getDefaultPattern(spinner.getLocale()));
}
```
Comment:
```
Creates a new <code>textcelleditor</code> instance.
```
---
id: 383

Code snippet:
```
void updateVisibilityModel(){
  Component c=getContainer();
  if (c instanceof JTextField) {
    JTextField field=(JTextField)c;
    BoundedRangeModel vis=field.getHorizontalVisibility();
    int hspan=(int)getPreferredSpan(X_AXIS);
    int extent=vis.getExtent();
    int maximum=Math.max(hspan,extent);
    extent=(extent == 0) ? maximum : extent;
    int value=maximum - extent;
    int oldValue=vis.getValue();
    if ((oldValue + extent) > maximum) {
      oldValue=maximum - extent;
    }
    value=Math.max(0,Math.min(value,oldValue));
    vis.setRangeProperties(value,extent,0,maximum,false);
  }
}
```
Comment:
```
Update the visibility model with the associated jtextfield (if there is one) to reflect the current visibility as a result of changes to the document model. the bounded range properties are updated. if the view hasn\'t yet been shown the extent will be zero and we just set it to be full until determined otherwise.
```
---
id: 384

Code snippet:
```
static int readInt(final byte[] b,final int index){
  return ((b[index] & 0xFF) << 24) | ((b[index + 1] & 0xFF) << 16) | ((b[index + 2] & 0xFF) << 8)| (b[index + 3] & 0xFF);
}
```
Comment:
```
Reads a signed int value in the given byte array.
```
---
id: 385

Code snippet:
```
public SQLDataException(String reason,String sqlState,int vendorCode){
  super(reason,sqlState,vendorCode);
}
```
Comment:
```
Creates an sqldataexception object. the reason string is set to the given reason string, the sqlstate string is set to the given sqlstate string and the error code is set to the given error code value.
```
---
id: 386

Code snippet:
```
public void test_readFully$BII() throws IOException {
  byte[] buf=new byte[10];
  oos.writeBytes(\"HelloWorld\");
  oos.close();
  ois=new ObjectInputStream(new ByteArrayInputStream(bao.toByteArray()));
  ois.readFully(buf,0,10);
  ois.close();
  assertEquals(\"Read incorrect bytes\",\"HelloWorld\",new String(buf,0,10,\"UTF-8\"));
}
```
Comment:
```
Java.io.objectinputstream#readfully(byte[], int, int).
```
---
id: 387

Code snippet:
```
public DTMStringPool(int chainSize){
  m_intToString=new Vector();
  m_hashChain=new IntVector(chainSize);
  removeAllElements();
  stringToIndex(\"\");
}
```
Comment:
```
Creates a new <code>tfloathashmap</code> instance.
```
---
id: 388

Code snippet:
```
public void encode(ByteStringBuilder buffer,EntryEncodeConfig config) throws DirectoryException {
  encodeV3(buffer,config);
}
```
Comment:
```
Encodes this entry into a form that is suitable for long-term persistent storage. the encoding will have a version number so that if the way we store entries changes in the future we will still be able to read entries encoded in an older format.
```
---
id: 389

Code snippet:
```
public synchronized void evictAll() throws IOException {
  initialize();
  for (  Entry entry : lruEntries.values().toArray(new Entry[lruEntries.size()])) {
    removeEntry(entry);
  }
}
```
Comment:
```
Removes all entries from the map.
```
---
id: 390

Code snippet:
```
public boolean compressAttributeDescriptions(){
  return compressAttrDescriptions;
}
```
Comment:
```
Indicates whether the encoded entry should use compressed attribute descriptions.
```
---
id: 391

Code snippet:
```
protected boolean shouldUpdateStyleOnEvent(PropertyChangeEvent ev){
  String eName=ev.getPropertyName();
  if (\"name\" == eName || \"componentOrientation\" == eName) {
    return true;
  }
  if (\"ancestor\" == eName && ev.getNewValue() != null) {
    return shouldUpdateStyleOnAncestorChanged();
  }
  return false;
}
```
Comment:
```
Returns true if the specified <code>jtextfield</code> is editable.
```
---
id: 392

Code snippet:
```
public boolean isExpanded(){
  return isExpanded;
}
```
Comment:
```
Gets the value of the isscorable property.
```
---
id: 393

Code snippet:
```
public DefaultRetryPolicy(int initialTimeoutMs,int maxNumRetries,float backoffMultiplier){
  mCurrentTimeoutMs=initialTimeoutMs;
  mMaxNumRetries=maxNumRetries;
  mBackoffMultiplier=backoffMultiplier;
}
```
Comment:
```
Constructs a new retry policy.
```
---
id: 394

Code snippet:
```
public void paintRootPaneBorder(SynthContext context,Graphics g,int x,int y,int w,int h){
  paintBorder(context,g,x,y,w,h,null);
}
```
Comment:
```
Paints the border of a split pane.
```
---
id: 395

Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(nodedocumenttypenodevalue.class,args);
}
```
Comment:
```
Runs this test from the command line.
```
---
id: 396

Code snippet:
```
public TitledBorder(Border border,String title,int titleJustification,int titlePosition){
  this(border,title,titleJustification,titlePosition,null,null);
}
```
Comment:
```
Creates a new border with the specified attributes.
```
---
id: 397

Code snippet:
```
@Override public AttributeSchemaImpl upgradeAttribute(AttributeSchemaImpl newAttr) throws UpgradeException {
  return updateDefaultValues(newAttr,Collections.singleton(OLDEST_VERSION));
}
```
Comment:
```
Gets the database specific sql attribute value.
```
---
id: 398

Code snippet:
```
public DefinitionDecodingException(AbstractManagedObjectDefinition<?,?> d,Reason reason){
  super(createLocalizableMessage(d,reason));
  this.d=d;
  this.reason=reason;
}
```
Comment:
```
Create a new definition decoding exception.
```
---
id: 399

Code snippet:
```
protected static String removeQuotes(String quotedString,boolean quotesRequired){
  if (quotedString.length() > 0 && quotedString.charAt(0) != \'\"\' && !quotesRequired) {
    return quotedString;
  }
 else   if (quotedString.length() > 2) {
    return quotedString.substring(1,quotedString.length() - 1);
  }
 else {
    return \"\";
  }
}
```
Comment:
```
Removes the quotes on a string. rfc2617 states quotes are optional for all parameters except realm.
```
---
