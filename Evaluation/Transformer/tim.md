id: 0

Code snippet:
```
public void UnexpectedTokenException(String token,LineCol lineCol) throws UnexpectedTokenException {
  if (fastFail)   throw new UnexpectedTokenException(buildErrInfo(lineCol),token,lineCol);
  String msg=\"unexpected token \" + token;
  msg=buildErrInfo(lineCol) + msg;
  error(msg + \" at \" + lineCol);
  errorList.add(new CompilingError(msg,lineCol,CompilingError.UnexpectedToken));
}
```
Comment:
```
This method is called when a patch operation is performed on the current service instance.
```
---
id: 1

Code snippet:
```
public boolean isValid(Object session) throws SessionException {
  debug.message(\"FedletSessionProvider.isValid called\");
  return false;
}
```
Comment:
```
Indicates whether the session is still valid. This is useful for toolkit clean-up thread.
```
---
id: 2

Code snippet:
```
public boolean isDirty(){
  return this.dirty.get();
}
```
Comment:
```
Whether or not there are unsaved changes.
```
---
id: 3

Code snippet:
```
public int size(){
  if (arrayTable == null) {
    return 0;
  }
  return arrayTable.size();
}
```
Comment:
```
Returns the number of elements in this list.
```
---
id: 4

Code snippet:
```
public CMSSignedData generate(String eContentType,CMSProcessable content,boolean encapsulate,Provider sigProvider) throws NoSuchAlgorithmException, CMSException {
  return generate(eContentType,content,encapsulate,sigProvider,true);
}
```
Comment:
```
generate a signed object that for a CMS Signed Data object using the given provider - if encapsulate is true a copy of the message will be included in the signature. The content type is set according to the OID represented by the string signedContentType.
```
---
id: 5

Code snippet:
```
@Override public boolean isLeapYear(long prolepticYear){
  return IsoChronology.INSTANCE.isLeapYear(prolepticYear + YEARS_DIFFERENCE);
}
```
Comment:
```
Checks if the specified year is a leap year. <p> Minguo leap years occur exactly in line with ISO leap years. This method does not validate the year passed in, and only has a well-defined result for years in the supported range.
```
---
id: 6

Code snippet:
```
public AsfHeader(final long pos,final BigInteger chunkLen,final long chunkCnt){
  super(GUID.GUID_HEADER,pos,chunkLen);
  this.chunkCount=chunkCnt;
}
```
Comment:
```
Creates a new <code>TObjectHeader</code> object
```
---
id: 7

Code snippet:
```
protected OrientationRequested(int value){
  super(value);
}
```
Comment:
```
Creates a new instance.
```
---
id: 8

Code snippet:
```
protected View createChild(String name){
  View view=null;
  if (name.equals(SEC_MH_COMMON)) {
    view=new CCSecondaryMasthead(this,name);
  }
 else   if (name.equals(PGTITLE)) {
    view=new CCPageTitle(this,ptModel,name);
  }
 else   if (ptModel.isChildSupported(name)) {
    view=ptModel.createChild(this,name);
  }
 else   if (name.equals(PROPERTY_ATTRIBUTE)) {
    view=new AMPropertySheet(this,propertySheetModel,name);
  }
 else   if (propertySheetModel.isChildSupported(name)) {
    view=propertySheetModel.createChild(this,name,getModel());
  }
 else {
    view=super.createChild(name);
  }
  return view;
}
```
Comment:
```
Creates user interface components used by this view bean.
```
---
id: 9

Code snippet:
```
public CallEndedEvent(Intent intent){
  super(EVENT_NAME,intent);
  Log.d(LOG_TAG,EVENT_NAME);
}
```
Comment:
```
Constructs a new CallEndedEvent object that holds an PHONE_CALL_ENDED event fired intent. This intent holds the data needed to check the event against user defined rules.
```
---
id: 10

Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  DocumentType docType;
  NamedNodeMap entities;
  Node entityNode;
  NamedNodeMap attrList;
  doc=(Document)load(\"staff\",false);
  docType=doc.getDoctype();
  assertNotNull(\"docTypeNotNull\",docType);
  entities=docType.getEntities();
  assertNotNull(\"entitiesNotNull\",entities);
  entityNode=entities.getNamedItem(\"ent1\");
  assertNotNull(\"ent1NotNull\",entityNode);
  attrList=entityNode.getAttributes();
  assertNull(\"entityAttributesNull\",attrList);
}
```
Comment:
```
Runs the test case.
```
---
id: 11

Code snippet:
```
public static final void addLoggingBehavior(LoggingBehavior behavior){
synchronized (loggingBehaviors) {
    loggingBehaviors.add(behavior);
  }
}
```
Comment:
```
Certain logging behaviors are available for debugging beyond those that should be enabled in production. Enables a particular extended logging in the sdk.
```
---
id: 12

Code snippet:
```
private void examineIncompleteOperation(ModifyDNOperation modifyDNOperation,ResultCode resultCode){
  assertEquals(modifyDNOperation.getResultCode(),resultCode);
  assertTrue(modifyDNOperation.getErrorMessage().length() > 0);
  assertTrue(modifyDNOperation.getProcessingStartTime() > 0);
  assertTrue(modifyDNOperation.getProcessingStopTime() > 0);
  assertTrue(modifyDNOperation.getProcessingTime() >= 0);
  assertTrue(modifyDNOperation.getErrorMessage().length() > 0);
  ensurePostReponseHasRun();
}
```
Comment:
```
Invokes a number of operation methods on the provided modify operation for which the pre-operation plugin was not called.
```
---
id: 13

Code snippet:
```
public Shape modelToView(int p0,Position.Bias b0,int p1,Position.Bias b1,Shape a) throws BadLocationException {
  return super.modelToView(p0,b0,p1,b1,adjustAllocation(a));
}
```
Comment:
```
Provides a mapping from the document model coordinate space to the coordinate space of the view mapped to it.
```
---
id: 14

Code snippet:
```
public static String rdnValue(RDN rdn){
  Reject.ifTrue(rdn.isMultiValued(),\"Multivalued RDNs not supported\");
  return rdn.getFirstAVA().getAttributeValue().toString();
}
```
Comment:
```
Returns a string representation of the given value.
```
---
id: 15

Code snippet:
```
private static void initializeParams(){
  String cacheSize=SystemProperties.get(CACHE_MAX_SIZE_KEY,CACHE_MAX_SIZE);
  try {
    maxSize=Integer.parseInt(cacheSize);
    if (maxSize < 1) {
      maxSize=CACHE_MAX_SIZE_INT;
    }
    if (DEBUG.messageEnabled()) {
      DEBUG.message(\"IdRemoteCachedServicesImpl.\" + \"intializeParams() Caching size set to: \" + maxSize);
    }
  }
 catch (  NumberFormatException ne) {
    maxSize=CACHE_MAX_SIZE_INT;
    if (DEBUG.warningEnabled()) {
      DEBUG.warning(\"IdRemoteCachedServicesImpl.initializeParams() - invalid value for cache size specified.\" + \" Setting to default value: \" + maxSize);
    }
  }
}
```
Comment:
```
Method to check if caching is enabled or disabled and configure the size of the cache accordingly.
```
---
id: 16

Code snippet:
```
public SCPolicyViewBean(){
  super(\"SCPolicy\",DEFAULT_DISPLAY_URL);
}
```
Comment:
```
Creates a policy configuration view bean.
```
---
id: 17

Code snippet:
```
public ComparisonFailure(String message,String expected,String actual){
  super(message);
  fExpected=expected;
  fActual=actual;
}
```
Comment:
```
Constructs a new exception with the specified detail message. The cause is not initialized.
```
---
id: 18

Code snippet:
```
@Override protected synchronized WZStreamingError startBroadcast(){
  getBroadcastConfig().setAudioChannels(isBluetoothActive() ? BLUETOOTH_CHANNELS : mStoredChannels);
  getBroadcastConfig().setAudioSampleRate(isBluetoothActive() ? BLUETOOTH_SAMPLE_RATE : mStoredSampleRate);
  return super.startBroadcast();
}
```
Comment:
```
Ensure broadcast config meets Bluetooth requirements
```
---
id: 19

Code snippet:
```
public boolean startedIdFound(){
  return startedIdFound;
}
```
Comment:
```
Returns <CODE>true</CODE> if the server start Id was found and <CODE>false</CODE> otherwise.
```
---
id: 20

Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  NodeList elementList;
  Node testEmployee;
  NamedNodeMap attributes;
  Attr domesticAttr;
  boolean specified;
  doc=(Document)load(\"staff\",false);
  elementList=doc.getElementsByTagName(\"address\");
  testEmployee=elementList.item(0);
  attributes=testEmployee.getAttributes();
  domesticAttr=(Attr)attributes.getNamedItem(\"domestic\");
  specified=domesticAttr.getSpecified();
  assertTrue(\"domesticSpecified\",specified);
}
```
Comment:
```
Runs the test case.
```
---
id: 21

Code snippet:
```
public OBJ_ADAPTER(String s,int minor,CompletionStatus completed){
  super(s,minor,completed);
}
```
Comment:
```
Creates a new instance of this class.
```
---
id: 22

Code snippet:
```
private Map toAvPairMap(Set<String> names,String token){
  if (token == null) {
    return Collections.EMPTY_MAP;
  }
  Map map=new HashMap();
  Set<String> set=new HashSet<String>();
  set.add(token);
  if (names == null || names.isEmpty()) {
    return map;
  }
  for (  final Object name : names) {
    map.put(name,set);
  }
  return map;
}
```
Comment:
```
Converts a set to a map, keys are the elements in the set, value is the token. User naming attribute is always added as one of the key.
```
---
id: 23

Code snippet:
```
private ChatFormat(char character){
  this(character,false);
}
```
Comment:
```
Constructs a color format for a color.
```
---
id: 24

Code snippet:
```
@SuppressWarnings(\"unchecked\") public void writeBlob(Blob x) throws SQLException {
  if (x == null) {
    attribs.add(null);
  }
 else {
    attribs.add(new SerialBlob(x));
  }
}
```
Comment:
```
Writes a <code>Blob</code> object in the Java programming language to this <code>SQLOutputImpl</code> object.  The driver converts it to a serializable <code>SerialBlob</code> SQL <code>BLOB</code> value before returning it to the database.
```
---
id: 25

Code snippet:
```
public synchronized boolean canUndoOrRedo(){
  if (indexOfNextAdd == edits.size()) {
    return canUndo();
  }
 else {
    return canRedo();
  }
}
```
Comment:
```
Gets the value of the isScorable property.
```
---
id: 26

Code snippet:
```
private boolean isCauseRecordDuplicatedException(Throwable ex,int maxLevels){
  return isCauseException(ex,ORecordDuplicatedException.class,maxLevels);
}
```
Comment:
```
Detect if the root cause of the exception is a duplicate record. This is necessary as the database may wrap this root cause in further exceptions, masking the underlying cause
```
---
id: 27

Code snippet:
```
@Override public void close() throws NamingException {
  getBoundContext().close();
}
```
Comment:
```
Closes the stream.
```
---
id: 28

Code snippet:
```
public Query or(List<Query> queries){
  innerQueries=queries;
  return this;
}
```
Comment:
```
Returns a list of documents that match the given query.
```
---
id: 29

Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  NodeList addrList;
  Node addrNode;
  boolean state;
  doc=(Document)load(\"staff\",false);
  addrList=doc.getElementsByTagName(\"address\");
  addrNode=addrList.item(0);
  state=addrNode.hasAttributes();
  assertTrue(\"throw_True\",state);
}
```
Comment:
```
Runs the test case.
```
---
id: 30

Code snippet:
```
@Action(name=\"status\",operationDescription=@Operation(description=RECORD_RESOURCE + \"operation.status.description\"),response=@Schema(schemaResource=\"RecordStatus.schema.json\")) public Promise<ActionResponse,ResourceException> actionStatus(Context serverContext,ActionRequest actionRequest){
  Record currentRecord=debugRecorder.getCurrentRecord();
  JsonObject jsonValue=JsonValueBuilder.jsonValue();
  if (currentRecord != null) {
    jsonValue.put(STATUS_LABEL,true);
    jsonValue.put(RECORD_LABEL,currentRecord.exportJson().asMap());
  }
 else {
    jsonValue.put(STATUS_LABEL,false);
  }
  return newResultPromise(newActionResponse(jsonValue.build()));
}
```
Comment:
```
Status action
```
---
id: 31

Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(nodegetprevioussiblingnull.class,args);
}
```
Comment:
```
Runs this test from the command line.
```
---
id: 32

Code snippet:
```
public boolean isGroupExecutable(){
  return is(encodedPermission,GROUP_EXECUTABLE);
}
```
Comment:
```
Gets the value of the vm property.
```
---
id: 33

Code snippet:
```
public FramedIPNetmaskAttribute(byte[] octets){
  super(octets);
  mask[0]=octets[2];
  mask[1]=octets[3];
  mask[2]=octets[4];
  mask[3]=octets[5];
}
```
Comment:
```
Constructs a new instance from the on-the-wire bytes for this attribute including the prefixing attribute-type code octet and length octet.
```
---
id: 34

Code snippet:
```
private static final <T>boolean insertMap(MapElement<T>[] oldMap,MapElement<T>[] newMap,MapElement<T> newElement){
  int pos=find(oldMap,newElement.name);
  if ((pos != -1) && (newElement.name.equals(oldMap[pos].name))) {
    return false;
  }
  System.arraycopy(oldMap,0,newMap,0,pos + 1);
  newMap[pos + 1]=newElement;
  System.arraycopy(oldMap,pos + 1,newMap,pos + 2,oldMap.length - pos - 1);
  return true;
}
```
Comment:
```
Inserts the specified element at the specified position in this list. Shifts the element currently at that position (if any) and any subsequent elements to the right (adds one to their indices).
```
---
id: 35

Code snippet:
```
public void assertDurationIsInRange(long expectedMillis){
  long minimum=(long)((double)expectedMillis * 0.90);
  long maximum=Math.max((long)((double)expectedMillis * 1.10),10);
  long waitMillis=Math.max(expectedMillis * 10,10);
  long duration=getDurationMillis(waitMillis);
  if (duration < minimum) {
    Assert.fail(\"expected duration: \" + expectedMillis + \" minimum duration: \"+ minimum+ \" actual duration too short: \"+ duration);
  }
 else   if (duration > maximum) {
    Assert.fail(\"expected duration: \" + expectedMillis + \" maximum duration: \"+ maximum+ \" actual duration too long: \"+ duration);
  }
}
```
Comment:
```
Asserts that the given long is within the inclusive range.
```
---
id: 36

Code snippet:
```
static <T>void any(Promise<T> parent,Promise<T>[] childPromises){
  final AtomicBoolean done=new AtomicBoolean();
  final Consumer<Promise<T>> runnable=null;
  for (  Promise<T> childPromise : childPromises) {
    childPromise.whenComplete(runnable);
  }
}
```
Comment:
```
Does the any logic for Any*Promise. If any child comes back, then the parent comes back.
```
---
id: 37

Code snippet:
```
public void visitMaxs(int maxStack,int maxLocals){
  if (mv != null) {
    mv.visitMaxs(maxStack,maxLocals);
  }
}
```
Comment:
```
Visits the maximum stack size and the maximum number of local variables of the method.
```
---
id: 38

Code snippet:
```
public void updateUI(){
  setUI((SeparatorUI)UIManager.getUI(this));
}
```
Comment:
```
Resets the UI property to a value from the current look and feel.
```
---
id: 39

Code snippet:
```
public void countDown(){
  sync.releaseShared(1);
}
```
Comment:
```
Decrements the count of the latch, releasing all waiting threads if the count reaches zero. <p>If the current count is greater than zero then it is decremented. If the new count is zero then all waiting threads are re-enabled for thread scheduling purposes. <p>If the current count equals zero then nothing happens.
```
---
id: 40

Code snippet:
```
public InvalidValue(){
  super();
}
```
Comment:
```
Constructs a new node for calculating the value of a number.
```
---
id: 41

Code snippet:
```
public boolean isFragment(){
  return fragment;
}
```
Comment:
```
Whether the tokens should be returned as a fragment of the URL.
```
---
id: 42

Code snippet:
```
public void readOID() throws IOException {
  if (tag != ASN1Constants.TAG_OID) {
    throw expected(\"OID\");
  }
  if (length < 1) {
    throw new ASN1Exception(\"Wrong length for ASN.1 object identifier at [\" + tagOffset + \"]\");
  }
  readContent();
  if ((buffer[offset - 1] & 0x80) != 0) {
    throw new ASN1Exception(\"Wrong encoding at [\" + (offset - 1) + \"]\");
  }
  oidElement=1;
  for (int i=0; i < length; i++, ++oidElement) {
    while ((buffer[contentOffset + i] & 0x80) == 0x80) {
      i++;
    }
  }
}
```
Comment:
```
Decodes ASN.1 ObjectIdentifier type
```
---
id: 43

Code snippet:
```
protected void updateNextObject(){
  if (!updateNextIndex()) {
    findNextValidParent();
  }
}
```
Comment:
```
Updates the current row.
```
---
id: 44

Code snippet:
```
public com.sun.identity.liberty.ws.common.jaxb.xmlsig.SignatureMethodElement createSignatureMethodElement() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.liberty.ws.common.jaxb.xmlsig.impl.SignatureMethodElementImpl();
}
```
Comment:
```
Create an instance of SignatureMethodElement
```
---
id: 45

Code snippet:
```
public void testRead3() throws Exception {
  byte[] data=new byte[]{-127,-100,-50,-10,-1,0,1,10,50,127};
  TestInputStream tis=new TestInputStream(data);
  CipherInputStream cis=new CipherInputStream(tis,new NullCipher());
  int expected=data.length;
  byte[] result=new byte[expected];
  int skip=2;
  int ind=skip;
  cis.read(null,0,skip);
  int got=skip + cis.read(result,0,1);
  while (true) {
    for (int j=0; j < got - ind; j++) {
      assertEquals(\"read(byte[] b, int off, int len) \" + \"returned incorrect data.\",result[j],data[ind + j]);
    }
    if (got == expected) {
      break;
    }
 else     if (got > expected) {
      fail(\"The data returned by \" + \"read(byte[] b, int off, int len) \" + \"is larger than expected.\");
    }
 else {
      ind=got;
      got+=cis.read(result,0,3);
    }
  }
  if (cis.read(result,0,1) != -1) {
    fail(\"read() should return -1 at the end of the stream.\");
  }
}
```
Comment:
```
read(byte[] b, int off, int len) method testing. Tests that method returns the correct value (related to the InputStream), that it discards bytes in the case of null buffer, and that it returns -1 at the end of stream.
```
---
id: 46

Code snippet:
```
public DNLock tryWriteLockSubtree(final DN subtree){
  return acquireLockFromCache(subtree).tryWriteLockSubtree();
}
```
Comment:
```
Returns the number of elements in the queue.
```
---
id: 47

Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(elementremoveattributerestoredefaultvalue.class,args);
}
```
Comment:
```
Runs this test from the command line.
```
---
id: 48

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
Cleans up the class loader.
```
---
id: 49

Code snippet:
```
public SecurityException(){
  super();
}
```
Comment:
```
Constructs a new exception with <code>null</code> as its detail message. The cause is not initialized.
```
---
id: 50

Code snippet:
```
public MLetContent(URL url,Map<String,String> attributes,List<String> types,List<String> values){
  this.documentURL=url;
  this.attributes=Collections.unmodifiableMap(attributes);
  this.types=Collections.unmodifiableList(types);
  this.values=Collections.unmodifiableList(values);
  String att=getParameter(\"codebase\");
  if (att != null) {
    if (!att.endsWith(\"/\")) {
      att+=\"/\";
    }
    try {
      baseURL=new URL(documentURL,att);
    }
 catch (    MalformedURLException e) {
    }
  }
  if (baseURL == null) {
    String file=documentURL.getFile();
    int i=file.lastIndexOf(\'/\');
    if (i >= 0 && i < file.length() - 1) {
      try {
        baseURL=new URL(documentURL,file.substring(0,i + 1));
      }
 catch (      MalformedURLException e) {
      }
    }
  }
  if (baseURL == null)   baseURL=documentURL;
}
```
Comment:
```
Creates a new <code>List</code> instance.
```
---
id: 51

Code snippet:
```
static void putCircleOfTrust(String realm,String name,CircleOfTrustDescriptor cotDescriptor){
  String classMethod=\"CircleOfTrustCache:putCircleOfTrust\";
  String cacheKey=buildCacheKey(realm,name);
  if (debug.messageEnabled()) {
    debug.message(classMethod + \": cacheKey = \" + cacheKey);
  }
  cotCache.put(cacheKey,cotDescriptor);
}
```
Comment:
```
Adds a new entry to the cache.
```
---
id: 52

Code snippet:
```
public byte readByte() throws SQLException {
  Byte attrib=(Byte)getNextAttribute();
  return (attrib == null) ? 0 : attrib.byteValue();
}
```
Comment:
```
Retrieves the next attribute in this <code>SQLInputImpl</code> object as a <code>byte</code> in the Java programming language. <p> This method does not perform type-safe checking to determine if the returned type is the expected type; this responsibility is delegated to the UDT mapping as defined by a <code>SQLData</code> implementation. <p>
```
---
id: 53

Code snippet:
```
private void initializeService(){
  try {
    readServiceConfig();
    Object[] cTypes=((Set)rawServiceData.get(LOCALE_CHARSET_ATTR)).toArray();
    for (int i=0; i < cTypes.length; i++) {
      createLocaleEntry((String)cTypes[i]);
    }
    cTypes=((Set)rawServiceData.get(CHARSET_ALIAS_ATTR)).toArray();
    for (int i=0; i < cTypes.length; i++) {
      createCharsetAliasEntry((String)cTypes[i]);
    }
  }
 catch (  SSOException ex) {
    debug.error(\"Unable to get internal SSOToken for locale attribute \",ex);
  }
catch (  SMSException ex) {
    debug.error(\"Unable to get  locale attribute value\",ex);
  }
}
```
Comment:
```
Initialize the configuration-specific supports Map.
```
---
id: 54

Code snippet:
```
public int compare(Object o1,Object o2){
  String s1=(String)o1;
  return (s1.compareTo((String)o2));
}
```
Comment:
```
Compares two objects
```
---
id: 55

Code snippet:
```
static <T>ReplayPromise<T> replayPromise(final Duration timeout,final long time){
  return new ReplayPromiseImpl<>(timeout,time);
}
```
Comment:
```
Returns a new instance with the specified duration.
```
---
id: 56

Code snippet:
```
public SAML2Exception(String message){
  super(message);
}
```
Comment:
```
Constructs a new <code>SAML2Exception</code> with the given message.
```
---
id: 57

Code snippet:
```
public static boolean isIPv6(String ipAddress){
  if (ipAddress == null || ipAddress.isEmpty()) {
    return false;
  }
  Matcher ipv6Matcher=IP_V6_PATTERN.matcher(ipAddress);
  return ipv6Matcher.find();
}
```
Comment:
```
Returns true if the given address is a valid email address.
```
---
id: 58

Code snippet:
```
public LifecycleException(){
  super();
}
```
Comment:
```
Constructs a new exception with <code>null</code> as its detail message. The cause is not initialized.
```
---
id: 59

Code snippet:
```
public TimeStampHeader createTimeStampHeader(float timeStamp) throws InvalidArgumentException {
  if (timeStamp < 0)   throw new IllegalArgumentException(\"illegal timeStamp\");
  TimeStamp t=new TimeStamp();
  t.setTimeStamp(timeStamp);
  return t;
}
```
Comment:
```
Creates a new TimeStampHeader based on the newly supplied timeStamp value.
```
---
id: 60

Code snippet:
```
public UnknownGroupException(String s){
  super(s);
}
```
Comment:
```
Creates a new instance of this class.
```
---
id: 61

Code snippet:
```
private void genericPostOperation(PostOperationOperation operation,DN dn){
  LDAPReplicationDomain domain=findDomain(dn,operation);
  if (domain != null) {
    domain.synchronize(operation);
  }
}
```
Comment:
```
Method findById.
```
---
id: 62

Code snippet:
```
static String keyToDNString(ByteString key){
  return key.toByteString().toASCIIString();
}
```
Comment:
```
Returns a best effort conversion from key to a human readable DN.
```
---
id: 63

Code snippet:
```
public LogConfigurationException(String message){
  super(message);
}
```
Comment:
```
Constructs a new exception with the specified detail message. The cause is not initialized.
```
---
id: 64

Code snippet:
```
public int showOpenDialog(Component parent) throws HeadlessException {
  setDialogType(OPEN_DIALOG);
  return showDialog(parent,null);
}
```
Comment:
```
Shows the dialog.
```
---
id: 65

Code snippet:
```
public boolean is_orthogonal(){
  return direction().is_orthogonal();
}
```
Comment:
```
Returns whether it has the value.
```
---
id: 66

Code snippet:
```
static boolean packageHasActivities(Context context,String packageName,UserHandleCompat user){
  final LauncherAppsCompat launcherApps=LauncherAppsCompat.getInstance(context);
  return launcherApps.getActivityList(packageName,user).size() > 0;
}
```
Comment:
```
Query the launcher apps service for whether the supplied package has MAIN/LAUNCHER activities in the supplied package.
```
---
id: 67

Code snippet:
```
public final Node popAndTop(){
  m_firstFree--;
  m_map[m_firstFree]=null;
  return (m_firstFree == 0) ? null : m_map[m_firstFree - 1];
}
```
Comment:
```
Pop a node from the tail of the vector and return the top of the stack after the pop.
```
---
id: 68

Code snippet:
```
private boolean verifySignature(String[] record,int signPos,int recPos) throws Exception {
  String curSign=record[signPos];
  byte[] prevMAC=helper.toByteArray(curMAC);
  byte[] newMAC;
  if ((prevSignature == null) || prevSignature.equals(\"\")) {
    newMAC=new byte[prevMAC.length];
    System.arraycopy(prevMAC,0,newMAC,0,prevMAC.length);
  }
 else {
    newMAC=new byte[prevMAC.length + helper.toByteArray(prevSignature).length];
    System.arraycopy(prevMAC,0,newMAC,0,prevMAC.length);
    System.arraycopy(helper.toByteArray(prevSignature),0,newMAC,prevMAC.length,helper.toByteArray(prevSignature).length);
  }
  if (recPos != 0) {
    prevSignature=curSign;
  }
  verified=helper.verifySignature(helper.toByteArray(curSign),newMAC);
  return verified;
}
```
Comment:
```
Verifies the signature entry in the log file for tampering.
```
---
id: 69

Code snippet:
```
private boolean removeElement(int s){
  int at=indexOf(s,0);
  if (at < 0)   return false;
  removeElementAt(at);
  return true;
}
```
Comment:
```
Removes the first occurrence of the argument from this vector. If the object is found in this vector, each component in the vector with an index greater or equal to the object\'s index is shifted downward to have an index one smaller than the value it had previously.
```
---
id: 70

Code snippet:
```
public void init(String hostedProviderId) throws FSAccountMgmtException {
  this.hostedProviderId=hostedProviderId;
  try {
    datastoreProvider=DataStoreProviderManager.getInstance().getDataStoreProvider(IFSConstants.IDFF);
  }
 catch (  Exception de) {
    FSUtils.debug.error(\"DefaultFSUserProvider.init: couldn\'t obtain \" + \"datastore provider:\",de);
    throw new FSAccountMgmtException(de.getMessage());
  }
}
```
Comment:
```
This method initializes this
```
---
id: 71

Code snippet:
```
public static boolean isHexDigit(byte b){
switch (b) {
case \'0\':
case \'1\':
case \'2\':
case \'3\':
case \'4\':
case \'5\':
case \'6\':
case \'7\':
case \'8\':
case \'9\':
case \'A\':
case \'B\':
case \'C\':
case \'D\':
case \'E\':
case \'F\':
case \'a\':
case \'b\':
case \'c\':
case \'d\':
case \'e\':
case \'f\':
    return true;
default :
  return false;
}
}
```
Comment:
```
Returns true if the given number is a number.
```
---
id: 72

Code snippet:
```
public com.sun.identity.saml2.jaxb.xmlsig.X509DataType.X509CRL createX509DataTypeX509CRL() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.saml2.jaxb.xmlsig.impl.X509DataTypeImpl.X509CRLImpl();
}
```
Comment:
```
Create an instance of X509DataTypeX509CRL
```
---
id: 73

Code snippet:
```
public VirtualStaticGroup(){
  super();
}
```
Comment:
```
Creates a new, uninitialized virtual static group instance.  This is intended for internal use only.
```
---
id: 74

Code snippet:
```
public static UIComponent createForm(){
  return JSFComponentFactory.createComponent(UIForm.COMPONENT_TYPE);
}
```
Comment:
```
Creates a new JSFComponent object.
```
---
id: 75

Code snippet:
```
public LDAPPostReadRequestControl(boolean isCritical,Set<String> rawAttributes){
  super(OID_LDAP_READENTRY_POSTREAD,isCritical);
  if (rawAttributes == null) {
    this.rawAttributes=new LinkedHashSet<>(0);
  }
 else {
    this.rawAttributes=rawAttributes;
  }
  requestedAttributes=null;
}
```
Comment:
```
Constructs a new exception with the specified detail message. The cause is not initialized.
```
---
id: 76

Code snippet:
```
private void sendEvent(Measurement measurement) throws IOException {
  final EventDSL event=riemannClient.event();
  event.service(measurement.name());
  event.state(\"ok\");
  event.metric(measurement.value());
  event.time(measurement.time());
  event.ttl(30);
  for (  Map.Entry<String,String> tag : measurement.tags().entrySet()) {
    event.tag(tag.getKey());
    event.attribute(tag.getKey(),tag.getValue());
  }
  for (  Map.Entry<String,String> field : measurement.fields().entrySet()) {
    event.attribute(field.getKey(),field.getValue());
  }
  riemannClient.sendEvent(event.build());
}
```
Comment:
```
Sends a message to the server.
```
---
id: 77

Code snippet:
```
@Fluent public Job done(){
  eventBus.send(Kue.workerAddress(\"done\",this),this.toJson());
  return this;
}
```
Comment:
```
Finish a job.
```
---
id: 78

Code snippet:
```
public SubCommandArgumentParser(String mainClassName,LocalizableMessage toolDescription,boolean longArgumentsCaseSensitive){
  super(mainClassName,toolDescription,longArgumentsCaseSensitive);
}
```
Comment:
```
Constructs a new exception with the specified detail message. The cause is not initialized.
```
---
id: 79

Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(characterdatagetdata.class,args);
}
```
Comment:
```
Runs this test from the command line.
```
---
id: 80

Code snippet:
```
private void writeListenerContents(ServerDescriptor desc){
  if (!isScriptFriendly()) {
    LocalizableMessage title=INFO_LISTENERS_TITLE.get();
    println(centerTitle(title));
  }
  Set<ConnectionHandlerDescriptor> allHandlers=desc.getConnectionHandlers();
  if (allHandlers.isEmpty()) {
    if (desc.getStatus() == ServerDescriptor.ServerStatus.STARTED) {
      if (!desc.isAuthenticated()) {
        println(INFO_NOT_AVAILABLE_AUTHENTICATION_REQUIRED_CLI_LABEL.get());
      }
 else {
        println(INFO_NO_LISTENERS_FOUND.get());
      }
    }
 else {
      println(INFO_NO_LISTENERS_FOUND.get());
    }
  }
 else {
    ConnectionHandlerTableModel connHandlersTableModel=new ConnectionHandlerTableModel(false);
    connHandlersTableModel.setData(allHandlers);
    writeConnectionHandlersTableModel(connHandlersTableModel,desc);
  }
}
```
Comment:
```
Writes the listeners contents displaying with what is specified in the provided ServerDescriptor object.
```
---
id: 81

Code snippet:
```
private void unSubscribeByEventType(Class eventType){
  List<Subscription> subscriptions=subscriptionsByEventType.get(eventType);
  if (subscriptions != null) {
    Iterator<Subscription> iterator=subscriptions.iterator();
    while (iterator.hasNext()) {
      Subscription subscription=iterator.next();
      if (subscription != null && !subscription.isUnsubscribed()) {
        subscription.unsubscribe();
        iterator.remove();
      }
    }
  }
}
```
Comment:
```
subscriptions unsubscribe
```
---
id: 82

Code snippet:
```
public int alloc(int size){
  int index=n;
  int len=array.length;
  if (n + size >= len) {
    byte[] aux=new byte[len + blockSize];
    System.arraycopy(array,0,aux,0,len);
    array=aux;
  }
  n+=size;
  return index;
}
```
Comment:
```
Allocate a new array.
```
---
id: 83

Code snippet:
```
public void addElement(Node value){
  if (!m_mutable)   throw new RuntimeException(XSLMessages.createXPATHMessage(XPATHErrorResources.ER_NODESET_NOT_MUTABLE,null));
  if ((m_firstFree + 1) >= m_mapSize) {
    if (null == m_map) {
      m_map=new Node[m_blocksize];
      m_mapSize=m_blocksize;
    }
 else {
      m_mapSize+=m_blocksize;
      Node newMap[]=new Node[m_mapSize];
      System.arraycopy(m_map,0,newMap,0,m_firstFree + 1);
      m_map=newMap;
    }
  }
  m_map[m_firstFree]=value;
  m_firstFree++;
}
```
Comment:
```
Append a Node onto the vector.
```
---
id: 84

Code snippet:
```
protected void PredicateExpr() throws javax.xml.transform.TransformerException {
  int opPos=m_ops.getOp(OpMap.MAPINDEX_LENGTH);
  appendOp(2,OpCodes.OP_PREDICATE);
  Expr();
  m_ops.setOp(m_ops.getOp(OpMap.MAPINDEX_LENGTH),OpCodes.ENDOP);
  m_ops.setOp(OpMap.MAPINDEX_LENGTH,m_ops.getOp(OpMap.MAPINDEX_LENGTH) + 1);
  m_ops.setOp(opPos + OpMap.MAPINDEX_LENGTH,m_ops.getOp(OpMap.MAPINDEX_LENGTH) - opPos);
}
```
Comment:
```
PredicateExpr ::= Expr
```
---
id: 85

Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  NamedNodeMap entities;
  DocumentType docType;
  Node retval;
  doc=(Document)load(\"hc_staff\",true);
  docType=doc.getDoctype();
  if (!((\"text/html\".equals(getContentType())))) {
    assertNotNull(\"docTypeNotNull\",docType);
    entities=docType.getEntities();
    assertNotNull(\"entitiesNotNull\",entities);
{
      boolean success=false;
      try {
        retval=entities.removeNamedItem(\"alpha\");
      }
 catch (      DOMException ex) {
        success=(ex.code == DOMException.NO_MODIFICATION_ALLOWED_ERR);
      }
      assertTrue(\"throw_NO_MODIFICATION_ALLOWED_ERR\",success);
    }
  }
}
```
Comment:
```
Runs the test case.
```
---
id: 86

Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  NodeList elementList;
  Node nameNode;
  CharacterData child;
  String badString;
  doc=(Document)load(\"hc_staff\",false);
  elementList=doc.getElementsByTagName(\"acronym\");
  nameNode=elementList.item(0);
  child=(CharacterData)nameNode.getFirstChild();
{
    boolean success=false;
    try {
      badString=child.substringData(-5,3);
    }
 catch (    DOMException ex) {
      success=(ex.code == DOMException.INDEX_SIZE_ERR);
    }
    assertTrue(\"throws_INDEX_SIZE_ERR\",success);
  }
}
```
Comment:
```
Runs the test case.
```
---
id: 87

Code snippet:
```
public boolean isFollowReferrals(){
  return followReferralsControl != null;
}
```
Comment:
```
Return true if this controller follows referrals.
```
---
id: 88

Code snippet:
```
public void updateUI(){
  setUI((ViewportUI)UIManager.getUI(this));
}
```
Comment:
```
Resets the UI property to a value from the current look and feel.
```
---
id: 89

Code snippet:
```
public Boolean isPassive(){
  return isPassive;
}
```
Comment:
```
Returns the value of the <code>isPassive</code> attribute.
```
---
id: 90

Code snippet:
```
public NSDictionary(){
  dict=new LinkedHashMap<String,NSObject>();
}
```
Comment:
```
Creates a new instance.
```
---
id: 91

Code snippet:
```
public MatteBorder(int top,int left,int bottom,int right,Color matteColor){
  super(top,left,bottom,right);
  this.color=matteColor;
}
```
Comment:
```
Creates a new instance.
```
---
id: 92

Code snippet:
```
public KeyStore loadKeyStore() throws KeyStoreException {
  KeyStore ks=null;
  try {
    KeyStoreBuilder builder=new KeyStoreBuilder();
    ks=builder.withKeyStoreFile(getKeyStoreFile()).withKeyStoreType(KeyStoreType.JCEKS).withPassword(getKeyPassword()).build();
  }
 catch (  IOException e) {
    throw new KeyStoreException(\"Could not initialize the Keystore\",e);
  }
  return ks;
}
```
Comment:
```
Creates a new instance.
```
---
id: 93

Code snippet:
```
boolean isValidated(){
  return schema != null;
}
```
Comment:
```
Indicates if the matching rule has been validated, which means it has a non-null schema.
```
---
id: 94

Code snippet:
```
synchronized void removeListener(String listenerID){
  if (listenerObjects != null) {
    listenerObjects.remove(listenerID);
    if (listenerObjects.isEmpty()) {
      SMSNotificationManager.getInstance().removeCallbackHandler(listenerId);
    }
  }
}
```
Comment:
```
Remove a notification listener.
```
---
id: 95

Code snippet:
```
public License(final String filename,final String text){
  if (filename == null) {
    throw new NullPointerException(\"license file name is null\");
  }
  if (filename.isEmpty()) {
    throw new IllegalArgumentException(\"license file name is empty\");
  }
  this.filename=filename;
  if (text == null) {
    throw new NullPointerException(\"license text is null\");
  }
  if (text.isEmpty()) {
    throw new IllegalArgumentException(\"license text is empty\");
  }
  this.text=text;
}
```
Comment:
```
Creates a new license with the given license text.
```
---
id: 96

Code snippet:
```
private void revealPanorama(){
  getView().setVisibility(View.VISIBLE);
  Animator circularReveal=ViewUtils.createCircularReveal(mRevealCenter,mRevealWidth,getView(),INTERPOLATOR);
  ObjectAnimator colorChange=ViewUtils.createColorChange(((FrameLayout)getView()),R.color.foreground,android.R.color.transparent,INTERPOLATOR);
  AnimatorSet animatorSet=new AnimatorSet();
  animatorSet.play(circularReveal).with(colorChange);
  animatorSet.start();
}
```
Comment:
```
Reveals the contents of this fragment using a circular reveal animation.
```
---
id: 97

Code snippet:
```
private static String asString(ByteBuffer buffer){
  final ByteBuffer copy=buffer.duplicate();
  final byte[] bytes=new byte[Math.min(copy.remaining(),50)];
  copy.get(bytes);
  return new String(bytes,StandardCharsets.UTF_8);
}
```
Comment:
```
Converts ByteBuffer to String
```
---
id: 98

Code snippet:
```
public static NSObject parse(File f) throws IOException, PropertyListFormatException {
  return parse(new FileInputStream(f));
}
```
Comment:
```
Parses a binary property list file.
```
---
id: 99

Code snippet:
```
public XACMLAuthzDecisionStatement createXACMLAuthzDecisionStatement(String xml) throws XACMLException {
  Object obj=XACMLSDKUtils.getObjectInstance(XACMLConstants.XACML_AUTHZ_DECISION_STATEMENT,xml);
  if (obj == null) {
    return new XACMLAuthzDecisionStatementImpl(xml);
  }
 else {
    return (XACMLAuthzDecisionStatement)obj;
  }
}
```
Comment:
```
Returns a new instance of <code>XACMLAuthzDecisionStatement</code>.  The return object is immutable.
```
---
