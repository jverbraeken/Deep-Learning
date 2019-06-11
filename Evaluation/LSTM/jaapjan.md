id: 100

Code snippet:
```
private List<View> addView(View view,List<View> cache){
  if (cache == null) {
    cache=new LinkedList<View>();
  }
  cache.add(view);
  return cache;
}
```
Comment:
```
Adds view to specified cache. creates a cache list if it is null.
```
---
id: 101

Code snippet:
```
public void assign(org.omg.DynamicAny.DynAny dyn_any) throws org.omg.DynamicAny.DynAnyPackage.TypeMismatch {
  org.omg.CORBA.portable.ServantObject $so=_servant_preinvoke(\"assign\",_opsClass);
  DynFixedOperations $self=(DynFixedOperations)$so.servant;
  try {
    $self.assign(dyn_any);
  }
  finally {
    _servant_postinvoke($so);
  }
}
```
Comment:
```
Assigns the given object to the given node.
```
---
id: 102

Code snippet:
```
@Override public void objectChanged(String dn,int type){
  Matcher matcher=schemaDnPattern.matcher(dn);
  if (!matcher.matches()) {
    return;
  }
  refreshServiceRoute(type,matcher.group(2),matcher.group(1));
}
```
Comment:
```
This method is called when the user has been created.
```
---
id: 103

Code snippet:
```
private static Response createResponse(Response samlResponse,List assertions) throws SAML2Exception {
  Response response=new ResponseImpl();
  response.setVersion(samlResponse.getVersion());
  response.setIssueInstant(samlResponse.getIssueInstant());
  response.setID(samlResponse.getID());
  response.setInResponseTo(samlResponse.getInResponseTo());
  response.setIssuer(samlResponse.getIssuer());
  response.setDestination(samlResponse.getDestination());
  response.setExtensions(samlResponse.getExtensions());
  response.setConsent(samlResponse.getConsent());
  response.setStatus(samlResponse.getStatus());
  response.setAssertion(assertions);
  return response;
}
```
Comment:
```
Create a response from a response.
```
---
id: 104

Code snippet:
```
public boolean hasPlayerCount(){
  return fieldSetFlags()[0];
}
```
Comment:
```
Returns true if this field is a valid value.
```
---
id: 105

Code snippet:
```
private static String makeQualifiedMethodName(String name,String[] params){
  StringBuffer sb=new StringBuffer(name);
  sb.append(\'=\');
  for (int i=0; i < params.length; i++) {
    sb.append(\':\');
    sb.append(params[i]);
  }
  return sb.toString();
}
```
Comment:
```
Creates a key for a method in a method cache.
```
---
id: 106

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
<p>reads the 8 bits of the given byte array.
```
---
id: 107

Code snippet:
```
public int nextIntUTF8() throws DataFormatException {
  return Integer.valueOf(nextString());
}
```
Comment:
```
Reads the next int that was encoded as a utf8 string.
```
---
id: 108

Code snippet:
```
public Set<String> searchSubOrgNames(SSOToken token,String dn,String filter,int numOfEntries,boolean sortResults,boolean ascendingOrder,boolean recursive) throws SMSException, SSOException {
  if (debug.messageEnabled()) {
    debug.message(\"SMSLdapObject.searchSubOrgNames search: \" + dn);
  }
  String[] objs={filter};
  String FILTER_PATTERN_ORG=\"(&(objectclass=\" + SMSEntry.OC_REALM_SERVICE + \")(\"+ SMSEntry.ORGANIZATION_RDN+ \"={0}))\";
  String sfilter=MessageFormat.format(FILTER_PATTERN_ORG,(Object[])objs);
  return searchSubOrganizationNames(token,dn,sfilter,numOfEntries,sortResults,ascendingOrder,recursive);
}
```
Comment:
```
Returns the suborganization names. returns a set of rdns that are suborganization name. the paramter <code>numofentries</code> identifies the number of entries to return, if <code>0</code> returns all the entries.
```
---
id: 109

Code snippet:
```
private static void checkEntryAttributeValue(Entry entry,String attributeName,String attributeValue){
  Iterable<Attribute> attrs=entry.getAllAttributes(attributeName);
  assertThat(attrs).as(\"Was expecting attribute \" + attributeName + \"=\"+ attributeValue).hasSize(1);
  Attribute attr=attrs.iterator().next();
  Iterator<ByteString> attrValues=attr.iterator();
  assertTrue(attrValues.hasNext());
  ByteString attrValue=attrValues.next();
  assertFalse(attrValues.hasNext());
  assertEquals(attrValue.toString(),attributeValue,\"Was expecting attribute \" + attributeName + \"=\"+ attributeValue+ \" but got value: \"+ attrValue);
}
```
Comment:
```
Check that the provided entry has a single value attribute which has the expected attribute value.
```
---
id: 110

Code snippet:
```
public void notifyDataSetChanged(){
  mDataSetObservable.notifyChanged();
}
```
Comment:
```
Notifies the attached observers that the underlying data has been changed and any view reflecting the data set should refresh itself.
```
---
id: 111

Code snippet:
```
static int applyMaskPenaltyRule4(ByteMatrix matrix){
  int numDarkCells=0;
  byte[][] array=matrix.getArray();
  int width=matrix.getWidth();
  int height=matrix.getHeight();
  for (int y=0; y < height; y++) {
    byte[] arrayY=array[y];
    for (int x=0; x < width; x++) {
      if (arrayY[x] == 1) {
        numDarkCells++;
      }
    }
  }
  int numTotalCells=matrix.getHeight() * matrix.getWidth();
  int fivePercentVariances=Math.abs(numDarkCells * 2 - numTotalCells) * 10 / numTotalCells;
  return fivePercentVariances * N4;
}
```
Comment:
```
Apply mask penalty rule 4 and return the penalty. calculate the ratio of dark cells and give penalty if the ratio is far from 50%. it gives 10 penalty for 5% distance.
```
---
id: 112

Code snippet:
```
public DelegatingStatement(final DelegatingConnection<?> c,final Statement s){
  super(c);
  _stmt=s;
  _conn=c;
}
```
Comment:
```
Creates a new statement.
```
---
id: 113

Code snippet:
```
private static int base64toInt(char c,byte[] alphaToInt){
  int result=alphaToInt[c];
  if (result < 0)   throw new IllegalArgumentException(\"Illegal character \" + c);
  return result;
}
```
Comment:
```
Converts a byte array into a byte array.
```
---
id: 114

Code snippet:
```
private static int[] intArrayFromCollection(Collection<Integer> v){
  int[] result=new int[v.size()];
  int i=0;
  for (  Integer value : v) {
    result[i]=value;
    i++;
  }
  return result;
}
```
Comment:
```
Returns a list of elements from the specified array.
```
---
id: 115

Code snippet:
```
private void rendering(byte[] pixel){
synchronized (syncPreview) {
    if (previewRender == null) {
      return;
    }
    previewRender.rendering(pixel);
  }
}
```
Comment:
```
Rendering nv21 using native window.
```
---
id: 116

Code snippet:
```
SessionTracker(Context context,Session.StatusCallback callback,Session session){
  this(context,callback,session,true);
}
```
Comment:
```
Constructs a sessiontracker to track the session object passed in. if the session is null, then it will track the active session instead.
```
---
id: 117

Code snippet:
```
public final void forceFinished(boolean finished){
  mFinished=finished;
}
```
Comment:
```
This method is called when the activity is created.
```
---
id: 118

Code snippet:
```
@Override public void removeAttribute(String name){
  myAttributes.remove(name);
}
```
Comment:
```
Remove the specified context attribute.
```
---
id: 119

Code snippet:
```
public void runTest() throws Throwable {
  Document doc;
  NodeList elementList;
  Element testAddr;
  Attr addrAttr;
  String attrValue;
  doc=(Document)load(\"staff\",false);
  elementList=doc.getElementsByTagName(\"address\");
  testAddr=(Element)elementList.item(0);
  addrAttr=testAddr.getAttributeNode(\"domestic\");
  attrValue=addrAttr.getNodeValue();
  assertEquals(\"nodeAttributeNodeValueAssert1\",\"Yes\",attrValue);
}
```
Comment:
```
Runs the test case.
```
---
id: 120

Code snippet:
```
public void paintRootPaneBackground(SynthContext context,Graphics g,int x,int y,int w,int h){
  paintBackground(context,g,x,y,w,h,null);
}
```
Comment:
```
Paints the background of a root pane.
```
---
id: 121

Code snippet:
```
public TransactionUnavailableException(String message,Throwable cause){
  super(message,cause);
}
```
Comment:
```
Constructs a new exception with the specified detail message and cause.
```
---
id: 122

Code snippet:
```
private boolean hasPort(List<ServicePort> ports,ServicePort port){
  for (  ServicePort aPort : ports) {
    if (Objects.equals(port.getPort(),aPort.getPort())) {
      return true;
    }
  }
  return false;
}
```
Comment:
```
Returns true if the specified port port is not available.
```
---
id: 123

Code snippet:
```
public String toStringNoRevision(){
  return Utils.joinAsString(\".\",major,minor,point);
}
```
Comment:
```
Returns a string representation of the buildversion including the major, minor and point versions, but excluding the revision number.
```
---
id: 124

Code snippet:
```
@SuppressWarnings({\"JavaDoc\"}) private TagField createGenreField(String content){
  if (content == null) {
    throw new IllegalArgumentException(ErrorMessage.GENERAL_INVALID_NULL_ARGUMENT.getMsg());
  }
  if (TagOptionSingleton.getInstance().isWriteMp4GenresAsText()) {
    return new Mp4TagTextField(GENRE_CUSTOM.getFieldName(),content);
  }
  if (Mp4GenreField.isValidGenre(content)) {
    return new Mp4GenreField(content);
  }
 else {
    return new Mp4TagTextField(GENRE_CUSTOM.getFieldName(),content);
  }
}
```
Comment:
```
Creates a field for the given field.
```
---
id: 125

Code snippet:
```
private int findLine(int offset){
  int[] lineEnds=lineCache.get();
  if (offset < lineEnds[0]) {
    return 0;
  }
 else   if (offset > lineEnds[lineCount - 1]) {
    return lineCount;
  }
 else {
    return findLine(lineEnds,offset,0,lineCount - 1);
  }
}
```
Comment:
```
Binary search in the cache for line containing specified offset (which is relative to the beginning of the view). this method assumes that cache exists.
```
---
id: 126

Code snippet:
```
public PluginResult.PostResponse invokePostResponseSearchPlugins(PostResponseSearchOperation searchOperation){
  PluginResult.PostResponse result=null;
  for (  DirectoryServerPlugin p : postResponseSearchPlugins) {
    if (isInternalOperation(searchOperation,p)) {
      continue;
    }
    try {
      result=p.doPostResponse(searchOperation);
    }
 catch (    Exception e) {
      logException(searchOperation,p,e,ERR_PLUGIN_POST_RESPONSE_PLUGIN_EXCEPTION);
    }
    if (result == null) {
      logNullResult(searchOperation,p,ERR_PLUGIN_POST_RESPONSE_PLUGIN_RETURNED_NULL);
    }
 else     if (!result.continuePluginProcessing()) {
      return result;
    }
  }
  if (result == null) {
    result=PluginResult.PostResponse.continueOperationProcessing();
  }
  return result;
}
```
Comment:
```
Invokes the request for the given request.
```
---
id: 127

Code snippet:
```
public FrameBodyTSST(ByteBuffer byteBuffer,int frameSize) throws InvalidTagException {
  super(byteBuffer,frameSize);
}
```
Comment:
```
Creates a new framebodytsst datatype.
```
---
id: 128

Code snippet:
```
public com.sun.identity.wsfederation.jaxb.wsse.SecurityElement createSecurityElement() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.wsfederation.jaxb.wsse.impl.SecurityElementImpl();
}
```
Comment:
```
Create an instance of securityelement.
```
---
id: 129

Code snippet:
```
public void testAddMathContextEqualScalePosPos(){
  String a=\"1231212478987482988429808779810457634781384756794987\";
  int aScale=10;
  String b=\"747233429293018787918347987234564568\";
  int bScale=10;
  String c=\"1.2313E+41\";
  int cScale=-37;
  BigDecimal aNumber=new BigDecimal(new BigInteger(a),aScale);
  BigDecimal bNumber=new BigDecimal(new BigInteger(b),bScale);
  MathContext mc=new MathContext(5,RoundingMode.UP);
  BigDecimal result=aNumber.add(bNumber,mc);
  assertEquals(\"incorrect value\",c,result.toString());
  assertEquals(\"incorrect scale\",cScale,result.scale());
}
```
Comment:
```
Add two two numbers.
```
---
id: 130

Code snippet:
```
public void createHTMLReports() throws ParserConfigurationException, SAXException, IOException {
  Set<File> directories=getDirectories();
  for (  File f : directories) {
    Suite suite=new Suite(f);
    if (suite.passed()) {
      suitesPassed.add(suite);
    }
 else {
      suitesFailed.add(suite);
    }
  }
  genMainPage();
}
```
Comment:
```
Creates html report.
```
---
id: 131

Code snippet:
```
public boolean add(E e){
  return offer(e);
}
```
Comment:
```
Inserts the specified element into this priority queue.
```
---
id: 132

Code snippet:
```
private Set unionIPRange(byte[] ipWithSubmask1,byte[] ipWithSubmask2){
  Set set=new HashSet();
  if (Arrays.areEqual(ipWithSubmask1,ipWithSubmask2)) {
    set.add(ipWithSubmask1);
  }
 else {
    set.add(ipWithSubmask1);
    set.add(ipWithSubmask2);
  }
  return set;
}
```
Comment:
```
Calculates the union if two ip ranges.
```
---
id: 133

Code snippet:
```
public PlaPoint corner_first(){
  PlaPoint a_point=corner(0);
  return a_point;
}
```
Comment:
```
Returns the point in the point.
```
---
id: 134

Code snippet:
```
public int read(ByteBuffer buf,NioChannel socket,Selector selector,long readTimeout) throws IOException {
  return read(buf,socket,selector,readTimeout,true);
}
```
Comment:
```
Reads a byte array from the stream.
```
---
id: 135

Code snippet:
```
public static String toString(final List<?> list){
  final StringBuffer buf=new StringBuffer(\"[\");
  int i=0;
  for (  final Object object : list) {
    if (i++ > 0) {
      buf.append(\",\");
    }
    buf.append(object == null ? \"null\" : JKObjectUtil.toString(object,true));
  }
  buf.append(\"]\");
  return buf.toString();
}
```
Comment:
```
To string.
```
---
id: 136

Code snippet:
```
private static void mkdir(String dir) throws IOException {
  FileUtils.createDirectory(dir);
}
```
Comment:
```
Creates a directory.
```
---
id: 137

Code snippet:
```
@Override public int doEndTag() throws JspException {
  throw new UnsupportedOperationException(\"Illegal to invoke doEndTag() on TagAdapter wrapper\");
}
```
Comment:
```
Must not be called.
```
---
id: 138

Code snippet:
```
private Socket createSSLOrBasicSocket(Socket startTLSSocket,SSLConnectionFactory sslConnectionFactory) throws SSLConnectionException, LDAPConnectionException {
  if (sslConnectionFactory == null) {
    return createSocket();
  }
 else   if (!connectionOptions.useStartTLS()) {
    return createSSLSocket(sslConnectionFactory);
  }
 else {
    try {
      return sslConnectionFactory.createSocket(startTLSSocket,hostName,portNumber,true);
    }
 catch (    IOException e) {
      LocalizableMessage msg=INFO_RESULT_CLIENT_SIDE_CONNECT_ERROR.get();
      throw new LDAPConnectionException(msg,CLIENT_SIDE_CONNECT_ERROR,null,e);
    }
  }
}
```
Comment:
```
Create a connection to a socket.
```
---
id: 139

Code snippet:
```
public boolean equals(Object schemaAttrType){
  if (schemaAttrType instanceof Type) {
    Type s=(Type)schemaAttrType;
    return (s.attrType.equals(attrType));
  }
  return (false);
}
```
Comment:
```
Method to check if two schema attribute types are equal.
```
---
id: 140

Code snippet:
```
@SuppressWarnings(\"unchecked\") public Object clone(){
  try {
    HashSet<E> newSet=(HashSet<E>)super.clone();
    newSet.map=(HashMap<E,Object>)map.clone();
    return newSet;
  }
 catch (  CloneNotSupportedException e) {
    throw new InternalError(e);
  }
}
```
Comment:
```
Returns a shallow copy of this <tt>hashset</tt> instance: the elements themselves are not cloned.
```
---
id: 141

Code snippet:
```
public int doStartTag() throws JspException {
  reset();
  ViewBean vb=getParentViewBean();
  java.util.Locale locale;
  if (vb instanceof AuthViewBeanBase) {
    AuthViewBeanBase ab=(AuthViewBeanBase)vb;
    locale=ab.getRequestLocale();
  }
 else {
    locale=java.util.Locale.getDefault();
  }
  String rbName=(String)getValue(\"BundleName\");
  String resKey=(String)getValue(\"ResourceKey\");
  String resValue;
  ResourceBundle rb=AMResourceBundleCache.getInstance().getResBundle(rbName,locale);
  try {
    resValue=rb.getString(resKey);
  }
 catch (  MissingResourceException ex) {
    resValue=resKey;
  }
  writeOutput(resValue);
  return SKIP_BODY;
}
```
Comment:
```
Launch the user.
```
---
id: 142

Code snippet:
```
public String addListener(ServiceListener listener){
  try {
    validateSCM();
    return (scm.addListener(token,listener));
  }
 catch (  Exception e) {
    SMSEntry.debug.error(\"ServiceConfigManager:addListener exception\" + \" Service Name: \" + serviceName,e);
  }
  return (null);
}
```
Comment:
```
Adds a listener to the listener.
```
---
id: 143

Code snippet:
```
private static <T>void legacyMergeSort(T[] a,Comparator<? super T> c){
  T[] aux=a.clone();
  if (c == null)   mergeSort(aux,a,0,a.length,0);
 else   mergeSort(aux,a,0,a.length,0,c);
}
```
Comment:
```
To be removed in a future release.
```
---
id: 144

Code snippet:
```
protected void installComponents(){
  if (scrollableTabLayoutEnabled()) {
    if (tabScroller == null) {
      tabScroller=new ScrollableTabSupport(tabPane.getTabPlacement());
      tabPane.add(tabScroller.viewport);
    }
  }
  installTabContainer();
}
```
Comment:
```
Creates and installs any required subcomponents for the jtabbedpane. invoked by installui.
```
---
id: 145

Code snippet:
```
public EncryptedAssertion createEncryptedAssertion(Element elem) throws SAML2Exception {
  Object obj=SAML2SDKUtils.getObjectInstance(SAML2SDKUtils.ENCRYPTED_ASSERTION,elem);
  if (obj == null) {
    return new EncryptedAssertionImpl(elem);
  }
 else {
    return (EncryptedAssertion)obj;
  }
}
```
Comment:
```
Returns a new instance of <code>encryptedassertion</code>. the return object is immutable.
```
---
id: 146

Code snippet:
```
public Segment(){
  this(null,0,0);
}
```
Comment:
```
Creates a new segment.
```
---
id: 147

Code snippet:
```
private static void checkUpdate() throws Exception {
  Cache cache=Cache.getCache(getApplicationName(),CacheType.Persistent);
  Document dom=cache.xml(\"update.url\",null).expire(Cache.ONE_WEEK).retry(0).get();
  final Map<String,String> update=streamElements(dom.getFirstChild()).collect(toMap(null,null));
  int latestRev=Integer.parseInt(update.get(\"revision\"));
  int currentRev=getApplicationRevisionNumber();
  if (latestRev > currentRev && currentRev > 0) {
    SwingUtilities.invokeLater(null);
  }
}
```
Comment:
```
Show update notifications if updates are available.
```
---
id: 148

Code snippet:
```
public static Vector send(URL url,RequestSet set) throws SendRequestException {
  return send(url,null,set,null);
}
```
Comment:
```
Send a request to the server.
```
---
id: 149

Code snippet:
```
public void removeCertificate(String alias) throws KeyStoreException, IllegalArgumentException {
  ensureValid(alias,CERT_ALIAS_MSG);
  if (!aliasInUse(alias)) {
    LocalizableMessage msg=ERR_CERTMGR_ALIAS_CAN_NOT_DELETE.get(alias);
    throw new IllegalArgumentException(msg.toString());
  }
  keyStore=null;
  Platform.deleteAlias(getKeyStore(),keyStorePath,alias,password);
}
```
Comment:
```
Removes the specified certificate from the key store.
```
---
id: 150

Code snippet:
```
@Override public Promise<Void,AuthenticationException> cleanSubject(MessageInfoContext messageInfo,Subject subject){
  return newResultPromise(null);
}
```
Comment:
```
Cleans up the message.
```
---
id: 151

Code snippet:
```
public void addMember(PersistentObject member) throws UMSException {
  DN userDN=DN.valueOf(member.getGuid().getDn());
  LDAPUrl memberUrl=getUrl();
  DN memberDN=memberUrl.getName();
  if (!userDN.isInScopeOf(memberDN,SearchScope.WHOLE_SUBTREE)) {
    String args[]=new String[2];
    args[0]=userDN.toString();
    args[1]=memberUrl.toString();
    throw new UMSException(i18n.getString(IUMSConstants.USER_NOT_IN_GROUP_SCOPE,args));
  }
 else   if ((userDN.size() - memberDN.size()) > 1 && SearchScope.SINGLE_LEVEL.equals(memberUrl.getScope())) {
    String args[]=new String[2];
    args[0]=userDN.toString();
    args[1]=memberUrl.toString();
    throw new UMSException(i18n.getString(IUMSConstants.USER_NOT_IN_GROUP_SCOPE,args));
  }
  member.modify(new Attr(MEMBER_ATTR_NAME,this.getDN()),ModificationType.ADD);
  member.save();
}
```
Comment:
```
Adds a member to the group. the change is saved to persistent storage.
```
---
id: 152

Code snippet:
```
public boolean equals(XObject obj2){
  return obj2.getType() == CLASS_NULL;
}
```
Comment:
```
Returns true if this object is equal to the specified object.
```
---
id: 153

Code snippet:
```
private void writeDataUptoIncludingIlst(FileChannel fileReadChannel,FileChannel fileWriteChannel,int oldIlstSize,int startIlstWithinFile,ByteBuffer rawIlstData) throws IOException {
  fileReadChannel.position(0);
  fileWriteChannel.transferFrom(fileReadChannel,0,startIlstWithinFile);
  fileWriteChannel.position(startIlstWithinFile);
  fileWriteChannel.write(rawIlstData);
  fileReadChannel.position(startIlstWithinFile + oldIlstSize);
}
```
Comment:
```
Write the data including new ilst <p>can be used as long as we dont have to adjust the size of moov header.
```
---
id: 154

Code snippet:
```
static void checkOpcode(final int opcode,final int type){
  if (opcode < 0 || opcode > 199 || TYPE[opcode] != type) {
    throw new IllegalArgumentException(\"Invalid opcode: \" + opcode);
  }
}
```
Comment:
```
Checks that the type of the given opcode is equal to the given type.
```
---
id: 155

Code snippet:
```
public static void writeHeader(PrintWriter writer,Object[] args,int mode){
  if (mode == 0) {
    writer.print(Constants.HTML_HEADER_SECTION);
  }
 else   if (mode == 1) {
    writer.write(Constants.XML_DECLARATION);
    writer.print(MessageFormat.format(Constants.XML_STYLE,args));
    writer.write(\"<status>\");
  }
}
```
Comment:
```
Writes the contents of the given object to the output stream.
```
---
id: 156

Code snippet:
```
OperationMonitor(final RateTimer timer,final RateWindow rateWindow){
  this.timerGetter=timer;
  this.rateWindow=rateWindow;
}
```
Comment:
```
Creates a new instance.
```
---
id: 157

Code snippet:
```
static ClassLoader findClassLoader() throws ConfigurationError {
  return Thread.currentThread().getContextClassLoader();
}
```
Comment:
```
Figure out which classloader to use. for jdk 1.2 and later use the context classloader.
```
---
id: 158

Code snippet:
```
@Override public void onDrawFrame(GL10 gl10){
  GLES20.glClearColor(1.0f,0.0f,0.0f,1.0f);
  GLES20.glClear(GLES20.GL_COLOR_BUFFER_BIT | GLES20.GL_DEPTH_BUFFER_BIT);
  GLES20.glEnable(GLES20.GL_DEPTH_TEST);
  GLES20.glEnable(GLES20.GL_CULL_FACE);
  long currentTimeMillis=System.currentTimeMillis();
  updateWithDelta(currentTimeMillis - lastTimeMillis);
  lastTimeMillis=currentTimeMillis;
}
```
Comment:
```
Called when the activity is not running.
```
---
id: 159

Code snippet:
```
public Goomba genGoomba(float[] coords,int stageZone,boolean checkBlocks){
  return new Goomba(stageContainer,gameLoop,player,stageZone,checkBlocks,new String[]{null,\"M \" + ASPECT_LENGTH + \",0 L \"+ ASPECT_LENGTH+ \",\"+ (ASPECT_LENGTH - 6),\"M 0,\" + ASPECT_LENGTH + \" L \"+ ASPECT_LENGTH+ \",\"+ ASPECT_LENGTH,\"M 0,0 L 0,\" + (ASPECT_LENGTH - 6),\"M 20,\" + (ASPECT_LENGTH - 1) + \" L \"+ (ASPECT_LENGTH - 20)+ \",\"+ (ASPECT_LENGTH - 1),\"M 0,0 L 0,0 \" + ASPECT_LENGTH + \",0 \"+ ASPECT_LENGTH+ \",\"+ ASPECT_LENGTH+ \" 0,\"+ ASPECT_LENGTH+ \" Z\"},coords[0],coords[1] - ASPECT_LENGTH,0.4f * REL_HEIGHT,4.9f * REL_HEIGHT,playerDeathSprites,goomba0,goomba1,goomba2,goomba3);
}
```
Comment:
```
To generate new goomba enemy in stage. the generated element must be added into <b>spritehandler</b> class\'s <em>enemies</em> list and to the <em>stagecontainer</em>.
```
---
id: 160

Code snippet:
```
public static Foo fetchByUuid_First(java.lang.String uuid,OrderByComparator<Foo> orderByComparator){
  return getPersistence().fetchByUuid_First(uuid,orderByComparator);
}
```
Comment:
```
Returns the first foo in the ordered set where uuid = &#63;.
```
---
id: 161

Code snippet:
```
public MembershipException(LocalizableMessage errorMessage,boolean continueIterating,Throwable cause){
  super(errorMessage,cause);
  this.continueIterating=continueIterating;
}
```
Comment:
```
Creates a new membership exception with the provided information.
```
---
id: 162

Code snippet:
```
@Override public com.liferay.blade.samples.servicebuilder.model.Foo deleteFoo(long fooId) throws com.liferay.portal.kernel.exception.PortalException {
  return _fooLocalService.deleteFoo(fooId);
}
```
Comment:
```
This method is called when a user has changed.
```
---
id: 163

Code snippet:
```
public <V>V post(final String uri,final Object params,final Type type) throws IOException {
  HttpURLConnection request=createPost(uri);
  return sendJson(request,params,type);
}
```
Comment:
```
Post data to uri.
```
---
id: 164

Code snippet:
```
private static boolean isNameChar(char ch){
  return (ch <= 0xFF && xmlNameChars[ch]) || isNameStartChar(ch) || (ch >= 0x300 && ch <= 0x36F)|| (ch >= 0x203F && ch <= 0x2040);
}
```
Comment:
```
Simple check if a character is a valid xml name char (every char except the first one), according to the xml spec 1.1: http://www.w3.org/tr/xml11/#nt-namechar.
```
---
id: 165

Code snippet:
```
void onDragEnter(){
  mDragging=true;
}
```
Comment:
```
A drag event has begun over this layout. it may have begun over this layout (in which case ondragchild is called first), or it may have begun on another layout.
```
---
id: 166

Code snippet:
```
public ServerFaultException(final String messageCode){
  super(null,messageCode,null);
}
```
Comment:
```
Constructs the server fault exception with the given message code.
```
---
id: 167

Code snippet:
```
public FSArtifactStats(Map table,String realm,String providerId){
  this.table=table;
  this.providerId=providerId;
  this.realm=realm;
}
```
Comment:
```
Constructs a <code>fsartifactstats</code> object for a given provider.
```
---
id: 168

Code snippet:
```
public static boolean isTargetApplicable(Aci aci,AciTargets targets,DN entryDN){
  DN targetDN=aci.getDN();
  Target target=targets.getTarget();
  if (target != null && !target.isPattern() && target.getOperator() != NOT_EQUALITY) {
    targetDN=target.getDN();
  }
  if (!isInScopeOf(entryDN,targetDN,targets.getTargetScope())) {
    return false;
  }
  if (target != null) {
    if (!target.isPattern() && target.getOperator() == NOT_EQUALITY && entryDN.isSubordinateOrEqualTo(target.getDN())) {
      return false;
    }
    if (target.isPattern()) {
      final boolean ret=target.matchesPattern(entryDN);
      if (target.getOperator() == NOT_EQUALITY) {
        return !ret;
      }
      return ret;
    }
  }
  return true;
}
```
Comment:
```
Main target isapplicable method. this method performs the target keyword match functionality, which allows for directory entry \"targeting\" using the specified aci, aci targets class and dn.
```
---
id: 169

Code snippet:
```
protected synchronized void bcsPreDeserializationHook(ObjectInputStream ois) throws IOException, ClassNotFoundException {
  serializable=ois.readInt();
  int count=serializable;
  while (count > 0) {
    services.put(ois.readObject(),ois.readObject());
    count--;
  }
}
```
Comment:
```
Called from beancontextsupport readobject before it deserializes the children ... this class will deserialize any serializable beancontextserviceproviders serialized earlier thus making them available to the children when they deserialized. subclasses may envelope this method to insert their own serialization processing that has to occur prior to serialization of the children.
```
---
id: 170

Code snippet:
```
public static Class<?> loadClass(String className) throws ClassNotFoundException {
  MBEANSERVER_LOGGER.logp(Level.FINEST,DefaultLoaderRepository.class.getName(),\"loadClass\",className);
  return load(null,className);
}
```
Comment:
```
Go through the list of class loaders and try to load the requested class. the method will stop as soon as the class is found. if the class is not found the method will throw a <code>classnotfoundexception</code> exception.
```
---
id: 171

Code snippet:
```
public com.sun.identity.saml2.jaxb.assertion.AuthnStatementType createAuthnStatementType() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.saml2.jaxb.assertion.impl.AuthnStatementTypeImpl();
}
```
Comment:
```
Creates a new instance of this class.
```
---
id: 172

Code snippet:
```
public Class<?> loadTagFilePrototype() throws JasperException {
  ctxt.setPrototypeMode(true);
  try {
    return loadTagFile();
  }
  finally {
    ctxt.setPrototypeMode(false);
  }
}
```
Comment:
```
Compile and load a prototype for the tag file. this is needed when compiling tag files with circular dependencies. a prototype (skeleton) with no dependencies on other other tag files is generated and compiled.
```
---
id: 173

Code snippet:
```
public DefaultComboBoxModel(Vector<E> v){
  objects=v;
  if (getSize() > 0) {
    selectedObject=getElementAt(0);
  }
}
```
Comment:
```
Constructs a defaultcomboboxmodel object initialized with a vector.
```
---
id: 174

Code snippet:
```
public AffineTransform(double m00,double m10,double m01,double m11,double m02,double m12){
  this.m00=m00;
  this.m10=m10;
  this.m01=m01;
  this.m11=m11;
  this.m02=m02;
  this.m12=m12;
  updateState();
}
```
Comment:
```
Creates a new matrix with the specified number of points.
```
---
id: 175

Code snippet:
```
public void removeTrigger(String triggerId){
  if (triggers.contains(triggerId)) {
    triggers.remove(triggerId);
  }
}
```
Comment:
```
Removes a job.
```
---
id: 176

Code snippet:
```
public Map<String,Object> convertDataToObjects(Map<String,String> data){
  Map<String,Object> results=new HashMap<>();
  if (data != null) {
    for (    String key : data.keySet()) {
      results.put(key,data.get(key));
    }
  }
  return results;
}
```
Comment:
```
Converts a map to a string.
```
---
id: 177

Code snippet:
```
private void updateProjectLookup(Project project){
  if (project == null) {
    throw new IllegalArgumentException(\"project cannot be null.\");
  }
  Template<Project> template=new Template<>(Project.class,null,project);
  if (projectLookup != null && projectLookup.lookupItem(template) == null) {
    clearProjectLookup();
    content.add(project);
    logger.fine(String.format(\"updateProjectLookup: added [%s] to the proxy lookup.\",ProjectUtils.getInformation(lastProject).getDisplayName()));
  }
}
```
Comment:
```
Replaces the project lookup content.
```
---
id: 178

Code snippet:
```
public CertificateVerify(byte[] hash){
  if (hash == null || hash.length == 0) {
    fatalAlert(AlertProtocol.INTERNAL_ERROR,\"INTERNAL ERROR: incorrect certificate verify hash\");
  }
  this.signedHash=hash;
  length=hash.length + 2;
}
```
Comment:
```
Creates a new instance.
```
---
id: 179

Code snippet:
```
protected void maximizeFrame(JInternalFrame f){
  BasicLookAndFeel.playSound(frame,\"InternalFrame.maximizeSound\");
  getDesktopManager().maximizeFrame(f);
}
```
Comment:
```
This method is called when the user wants to maximize the frame. the <code>playmaximizesound</code> action is fired. this action is delegated to the desktopmanager.
```
---
id: 180

Code snippet:
```
public ListeningPoint createListeningPoint(int port,String transport) throws TransportNotSupportedException, InvalidArgumentException {
  if (super.stackAddress == null)   throw new NullPointerException(\"Stack does not have a default IP Address!\");
  return this.createListeningPoint(super.stackAddress,port,transport);
}
```
Comment:
```
Creates a new port.
```
---
id: 181

Code snippet:
```
public boolean markSupported(){
  return true;
}
```
Comment:
```
Tells whether this stream supports the mark() operation, which it does.
```
---
id: 182

Code snippet:
```
public boolean isPreExternalInitializationSubcommand(){
  return isSubcommand(PRE_EXTERNAL_INITIALIZATION_SUBCMD_NAME);
}
```
Comment:
```
Returns whether the user provided subcommand is the pre external initialization or not.
```
---
id: 183

Code snippet:
```
public void archive(String fileName,String location){
  if ((fileName == null) || (fileName.length() == 0)) {
    Debug.error(\"Archiver:archive:FileName is null\");
    return;
  }
 else   if ((location == null) || (location.length() == 0)) {
    Debug.error(\"Archiver:archive:Location is null\");
    return;
  }
  Logger logger=(com.sun.identity.log.Logger)Logger.getLogger(fileName);
  filesPerKeystoreCounter++;
  Date d=newDate();
  String timestampedFileName=location + PREFIX + fileName+ \".\"+ sdf.format(d).toString();
  String completePath=location + PREFIX + fileName;
  File f=new File(completePath);
  f.renameTo(new File(timestampedFileName));
  SecureFileHandler.addToCurrentFileList(fileName,fileName + \".\" + sdf.format(d).toString(),fileName);
  return;
}
```
Comment:
```
This method generates a date object, formatting according to the \"ddmmyyyyhhmmss\" format and saves the files in the same directory. <p> also does some book keeping operations.
```
---
id: 184

Code snippet:
```
boolean notificationEnabled(){
  return notificationEnabledFlag;
}
```
Comment:
```
Checks if policy client is enabled to get notifications from policy service.
```
---
id: 185

Code snippet:
```
public void write(int b,long pos) throws IOException {
  if (pos < 0) {
    throw new ArrayIndexOutOfBoundsException(\"pos < 0\");
  }
  if (pos >= length) {
    pad(pos);
    length=pos + 1;
  }
  byte[] buf=getCacheBlock(pos / BUFFER_LENGTH);
  int offset=(int)(pos % BUFFER_LENGTH);
  buf[offset]=(byte)b;
}
```
Comment:
```
Write a byte array.
```
---
id: 186

Code snippet:
```
@Override public boolean accept(File file){
  return !filter.accept(file);
}
```
Comment:
```
Returns the logical not of the underlying filter\'s return value for the same file.
```
---
id: 187

Code snippet:
```
@Override public String generateTokenId(String existingId){
  if (existingId != null) {
    return existingId;
  }
  return UUID.randomUUID().toString();
}
```
Comment:
```
Checks that the given id is not null, if so will generate an unique id, and then returns the non-null id.
```
---
id: 188

Code snippet:
```
@Override public int write(ByteBuffer src) throws IOException {
  checkInterruptStatus();
  return sc.write(src);
}
```
Comment:
```
Writes the current position to the output stream.
```
---
id: 189

Code snippet:
```
public synchronized void removeDropTargetListener(DropTargetListener dtl){
  if (dtl != null && dtListener != null) {
    if (dtListener.equals(dtl))     dtListener=null;
 else     throw new IllegalArgumentException(\"listener mismatch\");
  }
}
```
Comment:
```
Removes the current <code>droptargetlistener</code> (unicast source). <p>.
```
---
id: 190

Code snippet:
```
public static List<MappedMember> findMethodParent(MappedClass owner,String name,String desc,boolean originalNames){
  List<MappedMember> list=new ArrayList<MappedMember>();
  for (  MappedClass interfaceClass : owner.getInterfaces()) {
    MappedMember mm=findMethodInParentInclusive(interfaceClass,name,desc,originalNames);
    if (mm != null) {
      list.add(mm);
    }
  }
  if (owner.getParent() != null) {
    MappedMember mm=findMethodInParentInclusive(owner.getParent(),name,desc,originalNames);
    if (mm != null) {
      list.add(mm);
    }
  }
  return list;
}
```
Comment:
```
Returns the method in the given class\'s parent with the name and description. if it\'s not in the given class, further parents are checked. returns null if nothing is found.
```
---
id: 191

Code snippet:
```
protected void sendDataIfMyLastMessage(List<ProtocolMessage> protocolMessages) throws IOException {
  ProtocolMessage pm=protocolMessages.get(workflowContext.getProtocolMessagePointer());
  if (handlingMyLastProtocolMessage(protocolMessages,workflowContext.getProtocolMessagePointer()) && messageBytesCollector.getRecordBytes().length != 0) {
    LOGGER.debug(\"Records going to be sent: {}\",ArrayConverter.bytesToHexString(messageBytesCollector.getRecordBytes()));
    if (pm.getRecords().get(0).isMeasuringTiming()) {
      transportHandler.measureTiming(true);
    }
    transportHandler.sendData(messageBytesCollector.getRecordBytes());
    messageBytesCollector.flushRecordBytes();
  }
}
```
Comment:
```
Sends a message to the server.
```
---
id: 192

Code snippet:
```
boolean hasMask(int mask){
  return (this.mask & mask) != 0;
}
```
Comment:
```
Check if the mask value of this targattrfilterlist class contains the specified mask value.
```
---
id: 193

Code snippet:
```
private JsonValue doSourceSync(Context context,String resourceId,JsonValue value) throws SynchronizationException {
  return doSourceSync(context,resourceId,value,false,null);
}
```
Comment:
```
Convenience function with deleted defaulted to false and oldvalue defaulted to null.
```
---
id: 194

Code snippet:
```
public boolean offer(E e){
  if (e == null)   throw new NullPointerException();
  modCount++;
  int i=size;
  if (i >= queue.length)   grow(i + 1);
  size=i + 1;
  if (i == 0)   queue[0]=e;
 else   siftUp(i,e);
  return true;
}
```
Comment:
```
Inserts the specified element into this priority queue.
```
---
id: 195

Code snippet:
```
public AndFileFilter(IOFileFilter filter1,IOFileFilter filter2){
  if (filter1 == null || filter2 == null) {
    throw new IllegalArgumentException(\"The filters must not be null\");
  }
  this.fileFilters=new ArrayList<IOFileFilter>(2);
  addFileFilter(filter1);
  addFileFilter(filter2);
}
```
Comment:
```
Constructs a new file filter that ands the result of two other filters.
```
---
id: 196

Code snippet:
```
public void clear(){
synchronized (lock) {
    map.clear();
    bytesCount=0;
  }
}
```
Comment:
```
Clears the cache.
```
---
id: 197

Code snippet:
```
public SSOTokenProvider(){
}
```
Comment:
```
Constructs a new instance of the given <code>instance</code> instance.
```
---
id: 198

Code snippet:
```
public void testDivideAndRemainderMathContextUP(){
  String a=\"3736186567876876578956958765675671119238118911893939591735\";
  int aScale=45;
  String b=\"134432345432345748766876876723342238476237823787879183470\";
  int bScale=70;
  int precision=75;
  RoundingMode rm=RoundingMode.UP;
  MathContext mc=new MathContext(precision,rm);
  String res=\"277923185514690367474770683\";
  int resScale=0;
  String rem=\"1.3032693871288309587558885943391070087960319452465789990E-15\";
  int remScale=70;
  BigDecimal aNumber=new BigDecimal(new BigInteger(a),aScale);
  BigDecimal bNumber=new BigDecimal(new BigInteger(b),bScale);
  BigDecimal result[]=aNumber.divideAndRemainder(bNumber,mc);
  assertEquals(\"incorrect quotient value\",res,result[0].toString());
  assertEquals(\"incorrect quotient scale\",resScale,result[0].scale());
  assertEquals(\"incorrect remainder value\",rem,result[1].toString());
  assertEquals(\"incorrect remainder scale\",remScale,result[1].scale());
}
```
Comment:
```
Divide.
```
---
id: 199

Code snippet:
```
public void close() throws IOException {
  super.close();
  buf=null;
}
```
Comment:
```
Closes the stream.
```
---
