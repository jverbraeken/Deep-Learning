id: 200

Code snippet:
```
public UnknownPropertyNameException(String message){
  super(message);
}
```
Comment:
```
Constructs a new exception with the specified detail message. the cause is not initialized.
```
---
id: 201

Code snippet:
```
public static String transliterate(final String value){
  validate(value,NULL_STRING_PREDICATE,NULL_STRING_MSG_SUPPLIER);
  String result=value;
  Set<Map.Entry<String,List<String>>> entries=Ascii.ascii.entrySet();
  for (  Map.Entry<String,List<String>> entry : entries) {
    for (    String ch : entry.getValue()) {
      result=result.replace(ch,entry.getKey());
    }
  }
  return result;
}
```
Comment:
```
Remove all non valid characters.
```
---
id: 202

Code snippet:
```
public static void enforceWhiteList(final Context context,final JsonValue jsonValue,final String objectType,final Set<String> validUserAttributes) throws BadRequestException {
  if (!context.containsContext(SelfServiceContext.class) || !objectType.equals(USER_TYPE)) {
    return;
  }
  final String realm=RealmContext.getRealm(context).asPath();
  if (validUserAttributes == null || validUserAttributes.isEmpty()) {
    throw new BadRequestException(\"Null/empty whitelist of valid attributes for self service user creation\");
  }
  IdentityDetails identityDetails=jsonValueToIdentityDetails(objectType,jsonValue,realm);
  Attribute[] attributes=identityDetails.getAttributes();
  for (  Attribute attribute : attributes) {
    if (!validUserAttributes.contains(attribute.getName())) {
      throw new BadRequestException(\"User attribute \" + attribute.getName() + \" is not valid for self service creation\");
    }
  }
}
```
Comment:
```
Kills the given user.
```
---
id: 203

Code snippet:
```
protected OpenDsException(Throwable cause){
  this(null,cause);
}
```
Comment:
```
Creates a new identified exception with the provided information.
```
---
id: 204

Code snippet:
```
public PdfDictionary copyTo(PdfDocument document,List<PdfName> excludeKeys,boolean allowDuplicating){
  Map<PdfName,PdfObject> excluded=new TreeMap<>();
  for (  PdfName key : excludeKeys) {
    PdfObject obj=map.get(key);
    if (obj != null)     excluded.put(key,map.remove(key));
  }
  PdfDictionary dictionary=copyTo(document,allowDuplicating);
  map.putAll(excluded);
  return dictionary;
}
```
Comment:
```
Copies dictionary to specified document. it\'s possible to pass a list of keys to exclude when copying.
```
---
id: 205

Code snippet:
```
public boolean isPureJAASModulePresent(final String configName,final Configuration configuration) throws AuthLoginException {
  if (enforceJAASThread) {
    return true;
  }
  if (null == configuration) {
    return true;
  }
  final AppConfigurationEntry[] entries=configuration.getAppConfigurationEntry(configName);
  if (entries == null) {
    throw new AuthLoginException(\"amAuth\",AMAuthErrorCode.AUTH_CONFIG_NOT_FOUND,null);
  }
  for (  AppConfigurationEntry entry : entries) {
    String className=entry.getLoginModuleName();
    if (debug.messageEnabled()) {
      debug.message(\"config entry: \" + className);
    }
    if (isPureJAASModule(className)) {
      return true;
    }
 else     if (!isISModule(className)) {
      categoriseModuleClassFromClassname(className);
      if (isPureJAASModule(className)) {
        return true;
      }
    }
  }
  return false;
}
```
Comment:
```
Returns whether the auth module is or the auth chain contains pure jaas module(s).
```
---
id: 206

Code snippet:
```
private AuthorizationIdentityResponseControl(final boolean isCritical,final String authorizationID){
  Reject.ifNull(authorizationID);
  this.isCritical=isCritical;
  this.authorizationID=authorizationID;
}
```
Comment:
```
Creates a new authenticator.
```
---
id: 207

Code snippet:
```
public static StringArgument trustStorePathArgument() throws ArgumentException {
  return trustStorePathArgument(null);
}
```
Comment:
```
Creates a new <code>coderresult</code> instance.
```
---
id: 208

Code snippet:
```
private boolean findNodeFromTail(Node node){
  Node t=tail;
  for (; ; ) {
    if (t == node)     return true;
    if (t == null)     return false;
    t=t.prev;
  }
}
```
Comment:
```
Returns whether the given node and the other object match. <p> the default implementation provided by this class tests whether the other object is a node of the same type with structurally isomorphic child subtrees. subclasses may override this method as needed. </p>.
```
---
id: 209

Code snippet:
```
public com.sun.identity.liberty.ws.common.jaxb.xmlenc.CipherReferenceType createCipherReferenceType() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.liberty.ws.common.jaxb.xmlenc.impl.CipherReferenceTypeImpl();
}
```
Comment:
```
Create an instance of cipherreferencetype.
```
---
id: 210

Code snippet:
```
@Override public String format(DateTimeFormatter formatter){
  Objects.requireNonNull(formatter,\"formatter\");
  return formatter.format(this);
}
```
Comment:
```
Formats a date using the specified formatter.
```
---
id: 211

Code snippet:
```
public static Reader newReader(ReadableByteChannel channel,CharsetDecoder decoder,int minBufferCapacity){
  return new InputStreamReader(new ChannelInputStream(channel),decoder);
}
```
Comment:
```
Returns a reader that decodes bytes from a channel.
```
---
id: 212

Code snippet:
```
@BeforeClass public void startServer() throws Exception {
  user1=DN.valueOf(\"cn=user1,dc=example,dc=com\");
  user2=DN.valueOf(\"cn=user2,dc=example,dc=com\");
  user3=DN.valueOf(\"cn=user3,dc=example,dc=com\");
  user4=DN.valueOf(\"cn=user4,dc=example,dc=com\");
  user5=DN.valueOf(\"cn=user5,dc=example,dc=com\");
  int resultCode=TestCaseUtils.applyModifications(true,\"dn: cn=schema\",\"changetype: modify\",\"add: attributeTypes\",\"attributeTypes: \" + TEST_TIME_DEF,\"attributeTypes: \" + TEST_DATE_DEF,\"-\",\"add: objectclasses\",\"objectclasses: \" + TEST_OC_DEF,\"objectclasses: \" + TEST_OC2_DEF);
  assertEquals(0,resultCode);
}
```
Comment:
```
Ensures that the directory server is running before executing the testcases.
```
---
id: 213

Code snippet:
```
public void compose(StylesheetRoot sroot) throws TransformerException {
  if (null == m_selectPattern && sroot.getOptimizer()) {
    XPath newSelect=rewriteChildToExpression(this);
    if (null != newSelect)     m_selectPattern=newSelect;
  }
  StylesheetRoot.ComposeState cstate=sroot.getComposeState();
  java.util.Vector vnames=cstate.getVariableNames();
  if (null != m_selectPattern)   m_selectPattern.fixupVariables(vnames,cstate.getGlobalsSize());
  if (!(m_parentNode instanceof Stylesheet) && m_qname != null) {
    m_index=cstate.addVariableName(m_qname) - cstate.getGlobalsSize();
  }
 else   if (m_parentNode instanceof Stylesheet) {
    cstate.resetStackFrameSize();
  }
  super.compose(sroot);
}
```
Comment:
```
This function is called after everything else has been recomposed, and allows the template to set remaining values that may be based on some other property that depends on recomposition.
```
---
id: 214

Code snippet:
```
Object processNCNAME(StylesheetHandler handler,String uri,String name,String rawName,String value,ElemTemplateElement owner) throws org.xml.sax.SAXException {
  if (getSupportsAVT()) {
    AVT avt=null;
    try {
      avt=new AVT(handler,uri,name,rawName,value,owner);
      if ((avt.isSimple()) && (!XML11Char.isXML11ValidNCName(value))) {
        handleError(handler,XSLTErrorResources.INVALID_NCNAME,new Object[]{name,value},null);
        return null;
      }
      return avt;
    }
 catch (    TransformerException te) {
      throw new org.xml.sax.SAXException(te);
    }
  }
 else {
    if (!XML11Char.isXML11ValidNCName(value)) {
      handleError(handler,XSLTErrorResources.INVALID_NCNAME,new Object[]{name,value},null);
      return null;
    }
    return value;
  }
}
```
Comment:
```
Process an attribute string of type ncname into a string.
```
---
id: 215

Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(elementsetattributenomodificationallowederrEE.class,args);
}
```
Comment:
```
Runs this test from the command line.
```
---
id: 216

Code snippet:
```
@Override public boolean isGroupingUsed(){
  return ndf.isGroupingUsed();
}
```
Comment:
```
Indicates whether grouping will be used in this format.
```
---
id: 217

Code snippet:
```
public void testGetSpanCount(){
  mRichTextView.formatSpan(0,5,RichTextView.FormatType.BOLD);
  assertEquals(1,mRichTextView.getSpanCount());
}
```
Comment:
```
Adds a span to the richtextview and verifies the getspancount method.
```
---
id: 218

Code snippet:
```
public int highestLayer(){
  if (getComponentCount() > 0)   return getLayer(getComponent(0));
  return 0;
}
```
Comment:
```
Returns the highest layer value from all current children. returns 0 if there are no children.
```
---
id: 219

Code snippet:
```
public void removeUpdate(DocumentEvent e,Shape a,ViewFactory f){
  super.removeUpdate(e,a,f);
}
```
Comment:
```
Gives notification that something was removed from the document in a location that this view is responsible for. if either parameter is <code>null</code>, behavior of this method is implementation dependent.
```
---
id: 220

Code snippet:
```
public void test_getInstanceLjava_lang_StringLjava_security_Provider01() throws Exception {
  for (  String validValue : getValidValues()) {
    try {
      TrustManagerFactory.getInstance(validValue,(Provider)null);
    }
 catch (    IllegalArgumentException expected) {
    }
  }
}
```
Comment:
```
Test for <code>getinstance(string algorithm, string provider)</code> method assertion: throws nullpointerexception when algorithm is null; throws nosuchalgorithmexception when algorithm is not correct;.
```
---
id: 221

Code snippet:
```
public AssertionArtifact createAssertionArtifact(String id,String destID,String targetUrl,String version) throws SAMLException {
  return createAssertionArtifact(id,destID,null,null,targetUrl,version);
}
```
Comment:
```
Creates an assertionartifact.
```
---
id: 222

Code snippet:
```
public FieldPosition(Format.Field attribute,int fieldID){
  this.attribute=attribute;
  this.field=fieldID;
}
```
Comment:
```
Creates a new instance of this class.
```
---
id: 223

Code snippet:
```
public AMSearchResults searchSubOrganizationalUnits(String wildcard,AMSearchControl searchControl) throws AMException, SSOException {
  return searchSubOrganizationalUnits(wildcard,null,searchControl);
}
```
Comment:
```
Searches for sub organizational units in this organizational unit using wildcards. wildcards can be specified such as a*, *, *a.
```
---
id: 224

Code snippet:
```
void checkDSDegradedStatus(){
  final int degradedStatusThreshold=localReplicationServer.getDegradedStatusThreshold();
  if (degradedStatusThreshold > 0) {
    for (    DataServerHandler serverHandler : connectedDSs.values()) {
      final int nChanges=serverHandler.getRcvMsgQueueSize();
      if (logger.isTraceEnabled()) {
        logger.trace(\"In RS \" + getLocalRSServerId() + \", for baseDN=\"+ getBaseDN()+ \": \"+ \"Status analyzer: DS \"+ serverHandler.getServerId()+ \" has \"+ nChanges+ \" message(s) in writer queue.\");
      }
      if (nChanges >= degradedStatusThreshold) {
        if (serverHandler.getStatus() == NORMAL_STATUS && changeStatus(serverHandler,TO_DEGRADED_STATUS_EVENT)) {
          break;
        }
      }
 else {
        if (serverHandler.getStatus() == DEGRADED_STATUS && changeStatus(serverHandler,TO_NORMAL_STATUS_EVENT)) {
          break;
        }
      }
    }
  }
}
```
Comment:
```
Checks if the current thread is in the queue.
```
---
id: 225

Code snippet:
```
public ContainerMBean() throws MBeanException, RuntimeOperationsException {
  super();
}
```
Comment:
```
Construct a <code>modelmbean</code> with default <code>modelmbeaninfo</code> information.
```
---
id: 226

Code snippet:
```
protected DeltaRequest deserializeDeltaRequest(DeltaSession session,byte[] data) throws ClassNotFoundException, IOException {
  session.lock();
  try {
    ReplicationStream ois=getReplicationStream(data);
    session.getDeltaRequest().readExternal(ois);
    ois.close();
    return session.getDeltaRequest();
  }
  finally {
    session.unlock();
  }
}
```
Comment:
```
Deserializes a session.
```
---
id: 227

Code snippet:
```
public boolean accept(File path){
  if (path.exists()) {
    if (path.isDirectory()) {
      return true;
    }
 else {
      String fileName=path.getName();
      return Utils.isMatch(fileName,fileNamePattern,wildCard);
    }
  }
  return false;
}
```
Comment:
```
Overrided method of filefilter to check whether to accept a path.
```
---
id: 228

Code snippet:
```
static void normalizeLangArray(XMPNode arrayNode){
  if (!arrayNode.getOptions().isArrayAltText()) {
    return;
  }
  for (int i=2; i <= arrayNode.getChildrenLength(); i++) {
    XMPNode child=arrayNode.getChild(i);
    if (child.hasQualifier() && X_DEFAULT.equals(child.getQualifier(1).getValue())) {
      try {
        arrayNode.removeChild(i);
        arrayNode.addChild(1,child);
      }
 catch (      XMPException e) {
        assert false;
      }
      if (i == 2) {
        arrayNode.getChild(2).setValue(child.getValue());
      }
      break;
    }
  }
}
```
Comment:
```
Normalizes an array of nodes.
```
---
id: 229

Code snippet:
```
public IMP_LIMIT(int minor,CompletionStatus completed){
  this(\"\",minor,completed);
}
```
Comment:
```
Constructs an <code>imp_limit</code> exception with the specified minor code and completion status.
```
---
id: 230

Code snippet:
```
public void createIDPDiscoveryConfig(String configFile,String templateFile,Properties properties) throws IOException {
  String content=getFileContent(templateFile);
  for (Iterator i=properties.keySet().iterator(); i.hasNext(); ) {
    String tag=(String)i.next();
    content=content.replaceAll(\"@\" + tag + \"@\",(String)properties.get(tag));
  }
  BufferedWriter out=new BufferedWriter(new FileWriter(configFile));
  out.write(content);
  out.close();
}
```
Comment:
```
Create a new server.
```
---
id: 231

Code snippet:
```
public boolean isMember(SSOToken token) throws SSOException {
  if (token == null) {
    return false;
  }
  if (!SSOTokenManager.getInstance().isValidToken(token)) {
    return false;
  }
  try {
    AMIdentity amId=IdUtils.getIdentity(token);
    IdType idType=amId.getType();
    if (debug.messageEnabled()) {
      debug.message(\"AuthenticatedAgents:isMember:idType = \" + idType + \", amId.getName() = \"+ amId.getName());
    }
    if (!idType.equals(IdType.AGENT)) {
      if (isSpecialUser(token.getPrincipal().getName())) {
        return true;
      }
      return false;
    }
  }
 catch (  IdRepoException ire) {
    debug.error(\"AuthenticatedAgents:isMember:IdRepoException:msg = \" + ire.getMessage());
    return false;
  }
  return true;
}
```
Comment:
```
Returns true if the user is authenticated.
```
---
id: 232

Code snippet:
```
public int size(){
  return hlist.size();
}
```
Comment:
```
Get the number of headers in the list.
```
---
id: 233

Code snippet:
```
public DomainDBCursor(final DN baseDN,final ReplicationDomainDB domainDB,CursorOptions options){
  this.baseDN=baseDN;
  this.domainDB=domainDB;
  this.options=options;
}
```
Comment:
```
Creates a new instance.
```
---
id: 234

Code snippet:
```
public String toString(){
  StringBuilder sb=new StringBuilder(100);
  sb.append(\"
Service Instance: \").append(getName()).append(\"
\tGroup: \").append(getGroup()).append(\"
\tURI: \").append(getURI()).append(\"
\tAttributes: \").append(getAttributes());
  return (sb.toString());
}
```
Comment:
```
String representation.
```
---
id: 235

Code snippet:
```
public String toXMLString() throws SAML2Exception {
  return this.toXMLString(true,false);
}
```
Comment:
```
Returns a string representation.
```
---
id: 236

Code snippet:
```
public void reset(){
  m_next=0;
}
```
Comment:
```
Resets the iterator to its initial state.
```
---
id: 237

Code snippet:
```
public FakeModdnOperation(CSN csn,Entry entry){
  super(csn);
  this.entry=entry;
}
```
Comment:
```
Creates a new fakemoddnoperation.
```
---
id: 238

Code snippet:
```
public void testObsoleteDstZoneName() throws Exception {
  SimpleDateFormat format=new SimpleDateFormat(\"yyyy-MM-dd\'T\'HH:mm zzzz\",Locale.US);
  Date normal=format.parse(\"1970-01-01T00:00 EET\");
  Date dst=format.parse(\"1970-01-01T00:00 EEST\");
  assertEquals(60 * 60 * 1000,normal.getTime() - dst.getTime());
}
```
Comment:
```
Africa/cairo standard time is eet and daylight time is eest. they no longer use their dst zone but we should continue to parse it properly.
```
---
id: 239

Code snippet:
```
public NClob readNClob() throws SQLException {
  return (NClob)getNextAttribute();
}
```
Comment:
```
Retrieves the next attribute in this <code>sqlinputimpl</code> object as a <code>sqlinputimpl</code> object in the java programming language. <p> this method does not perform type-safe checking to determine if the returned type is the expected type as this responsibility is delegated to the udt mapping as a <code>sqldata</code> implementation. <p>.
```
---
id: 240

Code snippet:
```
public XmlStreamWriter(File file,String defaultEncoding) throws FileNotFoundException {
  this(new FileOutputStream(file),defaultEncoding);
}
```
Comment:
```
Construct an new xml stream writer for the specified file with the specified default encoding.
```
---
id: 241

Code snippet:
```
static Object instantiate(Class<?> sibling,String className) throws InstantiationException, IllegalAccessException, ClassNotFoundException {
  ClassLoader cl=sibling.getClassLoader();
  Class<?> cls=ClassFinder.findClass(className,cl);
  return cls.newInstance();
}
```
Comment:
```
Try to create an instance of a named class. first try the classloader of \"sibling\", then try the system classloader then the class loader of the current thread.
```
---
id: 242

Code snippet:
```
public CachedBackupDirectory(File directory){
  directoryPath=directory.getPath();
  backupInfo=new File(directoryPath + File.separator + BACKUP_DIRECTORY_DESCRIPTOR_FILE);
  lastModified=-1;
  backupDirectory=null;
}
```
Comment:
```
Creates a new <code>cacheservercache</code>.
```
---
id: 243

Code snippet:
```
public void startRow(){
  rows.add(new ArrayList<String>());
  height++;
  column=0;
}
```
Comment:
```
Appends a new row to the table.
```
---
id: 244

Code snippet:
```
protected KeyPairGenerator(String algorithm){
  this.algorithm=algorithm;
}
```
Comment:
```
Creates a keypairgenerator object for the specified algorithm.
```
---
id: 245

Code snippet:
```
public Leaves(final Material type,TreeSpecies species,boolean isDecayable){
  super(type,species);
  setDecayable(isDecayable);
}
```
Comment:
```
Constructs a leaf block of the given type and tree species and flag for whether this leaf block will disappear when too far from a log.
```
---
id: 246

Code snippet:
```
Item newInteger(final int value){
  key.set(value);
  Item result=get(key);
  if (result == null) {
    pool.putByte(INT).putInt(value);
    result=new Item(index++,key);
    put(result);
  }
  return result;
}
```
Comment:
```
Adds a long to the constant pool of the class being build. does nothing if the constant pool already contains a similar item.
```
---
id: 247

Code snippet:
```
public long readLock(){
  long s=state, next;
  return ((whead == wtail && (s & ABITS) < RFULL && U.compareAndSwapLong(this,STATE,s,next=s + RUNIT)) ? next : acquireRead(false,0L));
}
```
Comment:
```
Returns the next available value.
```
---
id: 248

Code snippet:
```
public boolean isDefined(Object attrName){
  return table.containsKey(attrName);
}
```
Comment:
```
Returns <code>true</code> if this <code>tabulardata</code> is an <code>instanceof</code> object.
```
---
id: 249

Code snippet:
```
public void runTest() throws Throwable {
  String namespaceURI=\"http://www.nist.gov\";
  String qualifiedName=\"prefix:newAttr\";
  Document doc;
  Node arg;
  NodeList elementList;
  Node testAddress;
  NamedNodeMap attributes;
  Node retnode;
  String value;
  Node setNode;
  doc=(Document)load(\"staffNS\",true);
  arg=doc.createAttributeNS(namespaceURI,qualifiedName);
  arg.setNodeValue(\"newValue\");
  elementList=doc.getElementsByTagName(\"address\");
  testAddress=elementList.item(0);
  attributes=testAddress.getAttributes();
  setNode=attributes.setNamedItemNS(arg);
  retnode=attributes.getNamedItemNS(namespaceURI,\"newAttr\");
  value=retnode.getNodeValue();
  assertEquals(\"throw_Equals\",\"newValue\",value);
}
```
Comment:
```
Runs the test case.
```
---
id: 250

Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  Node rootNode;
  boolean state;
  doc=(Document)load(\"staff\",false);
  rootNode=doc.getDocumentElement();
  state=rootNode.isSupported(\"Core\",\"\");
  assertTrue(\"Core\",state);
}
```
Comment:
```
Runs the test case.
```
---
id: 251

Code snippet:
```
public static Border createLoweredSoftBevelBorder(){
  if (sharedSoftLoweredBevel == null) {
    sharedSoftLoweredBevel=new SoftBevelBorder(BevelBorder.LOWERED);
  }
  return sharedSoftLoweredBevel;
}
```
Comment:
```
Creates a bevel border with the current color.
```
---
id: 252

Code snippet:
```
public double length(){
  return Math.sqrt(NumberConversions.square(x) + NumberConversions.square(y) + NumberConversions.square(z));
}
```
Comment:
```
Returns the length of this vector.
```
---
id: 253

Code snippet:
```
public SQLTransientException(String reason,String sqlState,int vendorCode,Throwable cause){
  super(reason,sqlState,vendorCode,cause);
}
```
Comment:
```
Creates an sqltransientexception object. the reason string is set to the given reason string, the sqlstate string is set to the given sqlstate string and the cause throwable object is set to the given cause throwable object.
```
---
id: 254

Code snippet:
```
public void readAndExecute(LDAPConnection connection,List<String> lines,LDAPDeleteOptions deleteOptions) throws IOException, LDAPException {
  for (  String line : lines) {
    executeDelete(connection,line,deleteOptions);
  }
}
```
Comment:
```
Execute the delete request on the specified list of dns.
```
---
id: 255

Code snippet:
```
public boolean isNowWithinInterval(String intervalString) throws IllegalArgumentException {
  Interval interval=Interval.parse(intervalString);
  return interval.contains(DateTime.now());
}
```
Comment:
```
Returns true if this interval contains the specified interval.
```
---
id: 256

Code snippet:
```
public com.sun.identity.saml2.jaxb.assertion.BaseIDElement createBaseIDElement() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.saml2.jaxb.assertion.impl.BaseIDElementImpl();
}
```
Comment:
```
Create an instance of baseidelement.
```
---
id: 257

Code snippet:
```
public static RootContext ctx(){
  return new RootContext();
}
```
Comment:
```
Creates a root context to be passed in with client requests.
```
---
id: 258

Code snippet:
```
private void readObject(ObjectInputStream s) throws InvalidObjectException {
  throw new InvalidObjectException(\"Deserialization via serialization delegate\");
}
```
Comment:
```
Defend against malicious streams.
```
---
id: 259

Code snippet:
```
boolean isLiteral(Map attrs){
  if (!super.isLiteral(attrs)) {
    if (attrs == null) {
      return false;
    }
    int size=attrs.size();
    if (attrs.get(NumberFormat.Field.GROUPING_SEPARATOR) != null) {
      size--;
      if (attrs.get(NumberFormat.Field.INTEGER) != null) {
        size--;
      }
    }
    if (attrs.get(NumberFormat.Field.EXPONENT_SYMBOL) != null) {
      size--;
    }
    if (attrs.get(NumberFormat.Field.PERCENT) != null) {
      size--;
    }
    if (attrs.get(NumberFormat.Field.PERMILLE) != null) {
      size--;
    }
    if (attrs.get(NumberFormat.Field.CURRENCY) != null) {
      size--;
    }
    if (attrs.get(NumberFormat.Field.SIGN) != null) {
      size--;
    }
    return size == 0;
  }
  return true;
}
```
Comment:
```
Subclassed to treat the decimal separator, grouping separator, exponent symbol, percent, permille, currency and sign as literals.
```
---
id: 260

Code snippet:
```
public SQLiteCustomExtension(String path,String entryPoint){
  if (path == null) {
    throw new IllegalArgumentException(\"null path\");
  }
  this.path=path;
  this.entryPoint=entryPoint;
}
```
Comment:
```
Creates a sqlite extension description.
```
---
id: 261

Code snippet:
```
public static PlayerBucketEmptyEvent callPlayerBucketEmptyEvent(EntityHuman who,int clickedX,int clickedY,int clickedZ,EnumDirection clickedFace,ItemStack itemInHand){
  return (PlayerBucketEmptyEvent)getPlayerBucketEvent(false,who,clickedX,clickedY,clickedZ,clickedFace,itemInHand,Items.BUCKET);
}
```
Comment:
```
Bucket methods.
```
---
id: 262

Code snippet:
```
public LoginProcess(LoginAuthenticator loginAuthenticator,LoginConfiguration loginConfiguration,AuthenticationContext authContext,CoreServicesWrapper coreServicesWrapper){
  this.loginAuthenticator=loginAuthenticator;
  this.loginConfiguration=loginConfiguration;
  this.authContext=authContext;
  this.coreServicesWrapper=coreServicesWrapper;
}
```
Comment:
```
Creates a new instance.
```
---
id: 263

Code snippet:
```
public void test_hammerhead(){
  if (!android.os.Build.DEVICE.equals(\"hammerhead\")) {
    return;
  }
  assertEquals(mInvariantProfile.numRows,4);
  assertEquals(mInvariantProfile.numColumns,4);
  assertEquals((int)mInvariantProfile.numHotseatIcons,5);
  DeviceProfile landscapeProfile=mInvariantProfile.landscapeProfile;
  DeviceProfile portraitProfile=mInvariantProfile.portraitProfile;
  assertEquals(portraitProfile.allAppsNumCols,3);
  assertEquals(landscapeProfile.allAppsNumCols,5);
}
```
Comment:
```
Ensures that system calls (e.g., windowmanager, displaymetrics) that require contexts are properly working to generate minimum width and height of the display.
```
---
id: 264

Code snippet:
```
public EasyAppMod(final Context context){
  this.context=context;
}
```
Comment:
```
Instantiates a new easy app mod.
```
---
id: 265

Code snippet:
```
private static int nextHashCode(){
  return nextHashCode.getAndAdd(HASH_INCREMENT);
}
```
Comment:
```
Returns the next hash code.
```
---
id: 266

Code snippet:
```
public static String read(String fileName,Class cl){
  String data=\"\";
  try {
    InputStream in=cl.getResourceAsStream(fileName);
    if (in == null) {
      try {
        in=new FileInputStream(fileName);
      }
 catch (      FileNotFoundException e) {
        String directoryURL=cl.getProtectionDomain().getCodeSource().getLocation().toString();
        String fileURL=directoryURL + fileName;
        URL url=new URL(fileURL);
        in=url.openStream();
      }
    }
    data=Resource.read(new InputStreamReader(in));
    in.close();
  }
 catch (  Exception e) {
  }
  return data;
}
```
Comment:
```
Reads the resource from a class loader.
```
---
id: 267

Code snippet:
```
public FrameBodyTLAN(){
  super();
}
```
Comment:
```
Creates a new framebodytlan datatype.
```
---
id: 268

Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  Attr newAttrNode;
  String attrValue;
  String attrName;
  int attrType;
  doc=(Document)load(\"hc_staff\",true);
  newAttrNode=doc.createAttribute(\"title\");
  attrValue=newAttrNode.getNodeValue();
  assertEquals(\"value\",\"\",attrValue);
  attrName=newAttrNode.getNodeName();
  assertEqualsAutoCase(\"attribute\",\"name\",\"title\",attrName);
  attrType=(int)newAttrNode.getNodeType();
  assertEquals(\"type\",2,attrType);
}
```
Comment:
```
Runs the test case.
```
---
id: 269

Code snippet:
```
public static void copy(InputStream inputStream,OutputStream outputStream) throws IOException {
  copy(inputStream,outputStream,BUFFER_SIZE);
}
```
Comment:
```
Copies from input to output stream.
```
---
id: 270

Code snippet:
```
public QName(String localName){
  this(localName,false);
}
```
Comment:
```
Creates a new element.
```
---
id: 271

Code snippet:
```
public boolean isReal(){
  return type == REAL;
}
```
Comment:
```
Checks whether the value of this nsnumber is a real number.
```
---
id: 272

Code snippet:
```
public boolean isOwnerReadable(){
  return is(encodedPermission,OWNER_READABLE);
}
```
Comment:
```
Returns true if the user has permission.
```
---
id: 273

Code snippet:
```
protected int engineGetDigestLength(){
  return DIGEST_LENGTH;
}
```
Comment:
```
Returns a message digest length. <br> the method overrides \"enginegetdigestlength()\" in class messagedigestspi. <br>.
```
---
id: 274

Code snippet:
```
public Cursor fetch(Long eventID){
  if (eventID == null) {
    throw new IllegalArgumentException(\"primary key null.\");
  }
  Cursor mCursor=database.query(true,DATABASE_TABLE,KEYS,KEY_EVENTID + \"=\" + eventID,null,null,null,null,null);
  if (mCursor != null) {
    mCursor.moveToFirst();
  }
  return mCursor;
}
```
Comment:
```
Fetches the next row from the cursor.
```
---
id: 275

Code snippet:
```
protected boolean hasAttemptRemaining(){
  return mCurrentRetryCount <= mMaxNumRetries;
}
```
Comment:
```
Returns true if this policy has attempts remaining, false otherwise.
```
---
id: 276

Code snippet:
```
public void beginDisplay(DisplayEvent event) throws ModelControlException {
  super.beginDisplay(event);
  PWResetSuccessModel model=(PWResetSuccessModel)getModel();
  setDisplayFieldValue(CC_TITLE,model.getTitleString());
  setDisplayFieldValue(RESET_MESSAGE,resetMsg);
}
```
Comment:
```
Set the required information to display the page.
```
---
id: 277

Code snippet:
```
public CountingInputStream(final InputStream stream){
  super(stream);
  this.markPos=0;
  this.readCount=0;
}
```
Comment:
```
Creates a new instance.
```
---
id: 278

Code snippet:
```
public void postDeregister(){
}
```
Comment:
```
Register a new instance.
```
---
id: 279

Code snippet:
```
@Get public Representation endSession() throws OAuth2RestletException {
  final OAuth2Request request=requestFactory.create(getRequest());
  final String idToken=request.getParameter(OAuth2Constants.Params.END_SESSION_ID_TOKEN_HINT);
  final String redirectUri=request.getParameter(OAuth2Constants.Params.POST_LOGOUT_REDIRECT_URI);
  try {
    openIDConnectEndSession.endSession(request,idToken);
    if (StringUtils.isNotEmpty(redirectUri)) {
      return handleRedirect(request,idToken,redirectUri);
    }
  }
 catch (  OAuth2Exception e) {
    throw new OAuth2RestletException(e.getStatusCode(),e.getError(),e.getMessage(),null);
  }
  return null;
}
```
Comment:
```
Transforms the authenticateduser to a uri.
```
---
id: 280

Code snippet:
```
public boolean isLdaps(){
  return getConnectionType() == LDAPS;
}
```
Comment:
```
Returns whether this connection uses ldaps.
```
---
id: 281

Code snippet:
```
private TypeHelpCallback(AbstractManagedObjectDefinition<C,S> d){
  this.d=d;
}
```
Comment:
```
Creates a new instance.
```
---
id: 282

Code snippet:
```
private boolean isBleEnabled(){
  final BluetoothManager bm=(BluetoothManager)getActivity().getSystemService(Context.BLUETOOTH_SERVICE);
  final BluetoothAdapter ba=bm.getAdapter();
  return ba != null && ba.isEnabled();
}
```
Comment:
```
Gets the value of the enabled property.
```
---
id: 283

Code snippet:
```
public ID3v23Tag(ByteBuffer buffer,String loggingFilename) throws TagException {
  setLoggingFilename(loggingFilename);
  this.read(buffer);
}
```
Comment:
```
Creates a new id3v2_3 datatype.
```
---
id: 284

Code snippet:
```
public static RequirementsBuilder newArray(RequirementsBuilder builder){
  return newArray(0,builder,null);
}
```
Comment:
```
Creates a new builder.
```
---
id: 285

Code snippet:
```
private boolean isPreflightFlow(final HttpServletRequest req){
  final String reqMethodHeader=req.getHeader(CORSConstants.AC_REQUEST_METHOD);
  return CORSConstants.HTTP_OPTIONS.equals(req.getMethod()) && reqMethodHeader != null && !reqMethodHeader.isEmpty();
}
```
Comment:
```
Determines if this request should use the preflight flow or the normal flow. selects preflight if: <ul> <li>the method is of type options and <li>a header exists with the name access-control-request-method</code> and a value </ul>.
```
---
id: 286

Code snippet:
```
public com.sun.identity.saml2.jaxb.assertion.AttributeValueElement createAttributeValueElement() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.saml2.jaxb.assertion.impl.AttributeValueElementImpl();
}
```
Comment:
```
Creates a new element for the given element.
```
---
id: 287

Code snippet:
```
private static void changeBuildInfoVersion(final UpgradeContext context) throws ClientException {
  File buildInfoFile=new File(UpgradeUtils.configDirectory,Installation.BUILDINFO_RELATIVE_PATH);
  try (FileWriter buildInfo=new FileWriter(buildInfoFile,false)){
    buildInfo.write(context.getToVersion().toString());
    context.notify(INFO_UPGRADE_SUCCESSFUL.get(context.getFromVersion(),context.getToVersion()),TITLE_CALLBACK);
  }
 catch (  IOException e) {
    final LocalizableMessage message=LocalizableMessage.raw(e.getMessage());
    context.notify(message,ERROR_CALLBACK);
    throw new ClientException(ReturnCode.ERROR_UNEXPECTED,message);
  }
}
```
Comment:
```
Writes the up to date\'s version number within the build info file.
```
---
id: 288

Code snippet:
```
public static String convertID3v24GenreToGeneric(String value){
  try {
    int genreId=Integer.parseInt(value);
    if (genreId < GenreTypes.getMaxStandardGenreId()) {
      return GenreTypes.getInstanceOf().getValueForId(genreId);
    }
 else {
      return value;
    }
  }
 catch (  NumberFormatException nfe) {
    if (value.equalsIgnoreCase(ID3V2ExtendedGenreTypes.RX.name())) {
      value=ID3V2ExtendedGenreTypes.RX.getDescription();
    }
 else     if (value.equalsIgnoreCase(ID3V2ExtendedGenreTypes.CR.name())) {
      value=ID3V2ExtendedGenreTypes.CR.getDescription();
    }
 else {
      return value;
    }
  }
  return value;
}
```
Comment:
```
Convert a string value to a string.
```
---
id: 289

Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(hc_characterdatainsertdatabeginning.class,args);
}
```
Comment:
```
Runs this test from the command line.
```
---
id: 290

Code snippet:
```
public org.omg.CORBA.TCKind current_member_kind() throws org.omg.DynamicAny.DynAnyPackage.TypeMismatch, org.omg.DynamicAny.DynAnyPackage.InvalidValue {
  org.omg.CORBA.portable.ServantObject $so=_servant_preinvoke(\"current_member_kind\",_opsClass);
  DynValueOperations $self=(DynValueOperations)$so.servant;
  try {
    return $self.current_member_kind();
  }
  finally {
    _servant_postinvoke($so);
  }
}
```
Comment:
```
Returns the value of this attribute.
```
---
id: 291

Code snippet:
```
public ProxySelectorRoutePlanner(SchemeRegistry schreg,ProxySelector prosel){
  if (schreg == null) {
    throw new IllegalArgumentException(\"SchemeRegistry must not be null.\");
  }
  schemeRegistry=schreg;
  proxySelector=prosel;
}
```
Comment:
```
Instantiates a new powervmallocationpolicymigrationselector.
```
---
id: 292

Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(createDocumentType01.class,args);
}
```
Comment:
```
Runs this test from the command line.
```
---
id: 293

Code snippet:
```
public static boolean saveAttributes(final String filepath,Bundle bundle){
  ExifInterface exif;
  try {
    exif=new ExifInterface(filepath);
  }
 catch (  IOException e) {
    e.printStackTrace();
    return false;
  }
  for (  String tag : EXIF_TAGS) {
    if (bundle.containsKey(tag)) {
      exif.setAttribute(tag,bundle.getString(tag));
    }
  }
  try {
    exif.saveAttributes();
  }
 catch (  IOException e) {
    e.printStackTrace();
    return false;
  }
  return true;
}
```
Comment:
```
Store the exif attributes in the passed image file using the tags stored in the passed bundle.
```
---
id: 294

Code snippet:
```
private DN retrieveParentDNForAdd(final DN entryDN) throws DirectoryException {
  final DN parentDN=entryDN.parent();
  if (parentDN == null) {
    throw new DirectoryException(ResultCode.NO_SUCH_OBJECT,ERR_CONFIG_FILE_ADD_NO_PARENT_DN.get(entryDN));
  }
  if (!backend.contains(parentDN)) {
    throw new DirectoryException(ResultCode.NO_SUCH_OBJECT,ERR_CONFIG_FILE_ADD_NO_PARENT.get(entryDN,parentDN),getMatchedDN(parentDN),null);
  }
  return parentDN;
}
```
Comment:
```
Returns the parent dn of the configuration entry corresponding to the provided dn.
```
---
id: 295

Code snippet:
```
private static boolean valueEquals(Object obj1,Object obj2){
  if (obj1 == obj2) {
    return true;
  }
  if (obj1 == null) {
    return false;
  }
  if (obj1.getClass().isArray() && obj2.getClass().isArray()) {
    return arrayEquals(obj1,obj2);
  }
  return (obj1.equals(obj2));
}
```
Comment:
```
<p>compares two <code>object</code>s for equality.</p>.
```
---
id: 296

Code snippet:
```
public Builder withSystemSecurityManager(){
  return withSecurityManager(System.getSecurityManager());
}
```
Comment:
```
Returns a new instance of this class.
```
---
id: 297

Code snippet:
```
public String toString(){
  return oid.toString();
}
```
Comment:
```
Returns a string representation of the oid\'s integer components in dot separated notation.
```
---
id: 298

Code snippet:
```
private static String unCapitalize(String name){
  if (name == null || name.length() == 0) {
    return name;
  }
  char chars[]=name.toCharArray();
  chars[0]=Character.toLowerCase(chars[0]);
  return new String(chars);
}
```
Comment:
```
Converts the first character of the given string into lower-case.
```
---
id: 299

Code snippet:
```
public Assertion createAssertion(Object token) throws SAMLException {
  if (useLocal) {
    return (assertionManager.createAssertion(token));
  }
  String assertion=null;
  try {
    SessionProvider sessionProvider=SessionManager.getProvider();
    Object[] args={sessionProvider.getSessionID(token)};
    assertion=(String)stub.send(\"createAssertion\",args,null,null);
    return (new Assertion(XMLUtils.toDOMDocument(assertion,SAMLUtils.debug).getDocumentElement()));
  }
 catch (  Exception re) {
    if (SAMLUtils.debug.warningEnabled()) {
      SAMLUtils.debug.warning(\"AMC:createAssertion(SSO)\",re);
    }
    throw (new SAMLException(re.getMessage()));
  }
}
```
Comment:
```
Creates an instance of the associated element type.
```
---
