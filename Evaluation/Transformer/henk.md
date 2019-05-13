id: 300

Code snippet:
```
public void doGroupAction(Object obj){
  if (target != null) {
    target.doGroupAction(obj);
  }
}
```
Comment:
```
The function to be run on the objects when there is time.
```
---
id: 301

Code snippet:
```
public void appendQuotedExtension(StringBuffer toAddTo){
  appendQuoted(extension,toAddTo);
}
```
Comment:
```
<p>Append to the <code>toString</code> a <code>Writer</code> and a <code>Writer</code>.</p>
```
---
id: 302

Code snippet:
```
public R visitDuration(DurationPropertyDefinition pd,Long v,P p){
  return visitUnknown(pd,v,p);
}
```
Comment:
```
Returns a new instance with the specified number of minutes added. <p> This instance is immutable and unaffected by this method call.
```
---
id: 303

Code snippet:
```
@Inject public OpenIDConnectJWKEndpoint(OAuth2RequestFactory requestFactory,OAuth2ProviderSettingsFactory providerSettingsFactory,ExceptionHandler exceptionHandler){
  this.requestFactory=requestFactory;
  this.providerSettingsFactory=providerSettingsFactory;
  this.exceptionHandler=exceptionHandler;
}
```
Comment:
```
Constructs a new OpenIDConnectJWKEndpoint.
```
---
id: 304

Code snippet:
```
public static void askConfirmation(Context context,String title,String message,DialogInterface.OnClickListener onConfirm,DialogInterface.OnClickListener onCancel){
  new AlertDialog.Builder(context).setTitle(title).setMessage(message).setPositiveButton(android.R.string.ok,onConfirm).setNegativeButton(android.R.string.cancel,onCancel).show();
}
```
Comment:
```
Shows a confirmation dialog.
```
---
id: 305

Code snippet:
```
public boolean isEmpty(){
synchronized (lock) {
    return map.isEmpty();
  }
}
```
Comment:
```
Returns <tt>true</tt> if this MsgQueue contains no UpdateMsg.
```
---
id: 306

Code snippet:
```
public static KeyStoreHandler create(final File keyStoreFile,final char[] password) throws IOException, KeyStoreException {
  if (keyStoreFile == null) {
    throw new FileNotFoundException(null);
  }
 else   if (keyStoreFile.exists()) {
    throw new FileAlreadyExistsException(keyStoreFile.getAbsolutePath());
  }
  final KeyStore ks=KeyStore.getInstance(KeyStoreHandler.KEYSTORE_TYPE);
  try {
    ks.load(null,password);
  }
 catch (  final NoSuchAlgorithmException|CertificateException ex) {
    throw new IllegalStateException(\"Should not happen.\",ex);
  }
  final SecretKeyFactory skf=KeyStoreHandler.getSecretKeyFactory();
  final KeyStoreHandler ksh=new KeyStoreHandler(ks,password,keyStoreFile,skf,true);
  ksh.save();
  return ksh;
}
```
Comment:
```
Creates a new <code>JarFile</code> object
```
---
id: 307

Code snippet:
```
protected void release(DirContext context){
}
```
Comment:
```
Releases the given object.
```
---
id: 308

Code snippet:
```
private void finishedDispatching(boolean dispatched){
  this.dispatched=dispatched;
  if (notifier != null) {
synchronized (notifier) {
      notifier.notifyAll();
    }
  }
  if (listener != null) {
    listener.run();
  }
}
```
Comment:
```
Called when the event was dispatched or disposed
```
---
id: 309

Code snippet:
```
public static XMPMeta parseFromString(String packet,ParseOptions options) throws XMPException {
  return XMPMetaParser.parse(packet,options);
}
```
Comment:
```
Parses the specified string as a signed short value using the specified radix. The ASCII character \u002d (\'-\') is recognized as the minus sign.
```
---
id: 310

Code snippet:
```
public PdfOCProperties(PdfDictionary ocPropertiesDict){
  super(ocPropertiesDict);
  ensureObjectIsAddedToDocument(ocPropertiesDict);
  readLayersFromDictionary();
}
```
Comment:
```
Creates a new PdfOCProperties instance by the dictionary it represents, the dictionary must be an indirect object.
```
---
id: 311

Code snippet:
```
public static JPasswordField createPasswordField(int cols){
  JPasswordField pf=createPasswordField();
  pf.setColumns(cols);
  return pf;
}
```
Comment:
```
Creates a new instance of this class.
```
---
id: 312

Code snippet:
```
@Override public Foo findByUuid_Last(String uuid,OrderByComparator<Foo> orderByComparator) throws NoSuchFooException {
  Foo foo=fetchByUuid_Last(uuid,orderByComparator);
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
Returns the last foo in the ordered set where uuid = &#63;.
```
---
id: 313

Code snippet:
```
public void delete() throws IOException {
  close();
  fileSystem.deleteContents(directory);
}
```
Comment:
```
Closes the cache and deletes all of its stored values. This will delete all files in the cache directory including files that weren\'t created by the cache.
```
---
id: 314

Code snippet:
```
@Override public Call<GeocodingResponse> cloneCall(){
  return getCall().clone();
}
```
Comment:
```
Deep clone
```
---
id: 315

Code snippet:
```
public static ImmutableMap<String,InitValueConfig> createCollectionMap(MethodTransformerContext context){
  ImmutableMap.Builder<String,InitValueConfig> mapBuilder=ImmutableMap.builder();
  Map<String,String> fieldNamePatterns=context.getMethodConfig().getFieldNamePatterns();
  for (  Map.Entry<String,String> fieldNamePattern : fieldNamePatterns.entrySet()) {
    CollectionConfig collectionConfig=context.getCollectionConfig(fieldNamePattern.getValue());
    String apiWrapperClassName=context.getNamer().getApiWrapperClassName(context.getInterface());
    InitValueConfig initValueConfig=InitValueConfig.create(apiWrapperClassName,collectionConfig);
    mapBuilder.put(fieldNamePattern.getKey(),initValueConfig);
  }
  return mapBuilder.build();
}
```
Comment:
```
A utility method which creates the InitValueConfig map that contains the collection config data.
```
---
id: 316

Code snippet:
```
@BeforeClass public void startServer() throws Exception {
  TestCaseUtils.startServer();
  dictionaryFile=TestCaseUtils.createTempFile(\"love\",\"sex\",\"secret\",\"god\",\"password\");
}
```
Comment:
```
Ensures that the Directory Server is running.  Also, create a very small test dictionary file to use for the test cases so we don\'t suffer from loading the real word list every time.
```
---
id: 317

Code snippet:
```
public PlaSegmentFloat translate(double p_dist){
  double dx=point_b.v_x - point_a.v_x;
  double dy=point_b.v_y - point_a.v_y;
  double dxdx=dx * dx;
  double dydy=dy * dy;
  double lenght=Math.sqrt(dxdx + dydy);
  PlaPointFloat new_a;
  if (dxdx <= dydy) {
    double rel_x=(p_dist * lenght) / dy;
    new_a=new PlaPointFloat(point_a.v_x - rel_x,point_a.v_y);
  }
 else {
    double rel_y=(p_dist * lenght) / dx;
    new_a=new PlaPointFloat(point_a.v_x,point_a.v_y + rel_y);
  }
  PlaPointFloat new_b=new PlaPointFloat(new_a.v_x + dx,new_a.v_y + dy);
  return new PlaSegmentFloat(new_a,new_b);
}
```
Comment:
```
translates the line perpendicular at about p_dist. If p_dist > 0, the line will be translated to the left, else to the right
```
---
id: 318

Code snippet:
```
public ActionMap(){
}
```
Comment:
```
Creates an <code>ActionMap</code> with no parent and no mappings.
```
---
id: 319

Code snippet:
```
public synchronized NSObject member(NSObject obj){
  for (  NSObject o : set) {
    if (o.equals(obj))     return o;
  }
  return null;
}
```
Comment:
```
Determines whether the set contains an object equal to a given object and returns that object if it is present.
```
---
id: 320

Code snippet:
```
protected void completeDrag(MouseEvent e){
  finishDraggingTo(positionForMouseEvent(e));
}
```
Comment:
```
Invoked when a mouse button has been released.
```
---
id: 321

Code snippet:
```
public OrderService initializePersistence(Handler<AsyncResult<Void>> resultHandler){
  delegate.initializePersistence(resultHandler);
  return this;
}
```
Comment:
```
Initialize the persistence.
```
---
id: 322

Code snippet:
```
public SSOToken createSSOToken(javax.servlet.http.HttpServletRequest request) throws UnsupportedOperationException, SSOException {
  for (  SSOProviderPlugin ssoProvider : getSsoProviderPlugins()) {
    if (ssoProvider.isApplicable(request)) {
      return ssoProvider.createSSOToken(request);
    }
  }
  if (dProProvider != null)   return (dProProvider.createSSOToken(request));
 else   return (grappaProvider.createSSOToken(request));
}
```
Comment:
```
Creates a single sign on token from <code>HttpServletRequest</code>
```
---
id: 323

Code snippet:
```
public void dispose(){
  close_files();
  gdi_context=null;
  coordinate_transform=null;
  itera_settings=null;
  interactive_state=null;
  ratsnest=null;
  clearance_violations=null;
  r_board=null;
}
```
Comment:
```
Frees allocated resources.
```
---
id: 324

Code snippet:
```
public void runTest() throws Throwable {
  String namespaceURI=null;
  String qualifiedName=\"prefix:local\";
  Document doc;
  Attr newAttr;
  doc=(Document)load(\"staffNS\",false);
{
    boolean success=false;
    try {
      newAttr=doc.createAttributeNS(namespaceURI,qualifiedName);
    }
 catch (    DOMException ex) {
      success=(ex.code == DOMException.NAMESPACE_ERR);
    }
    assertTrue(\"throw_NAMESPACE_ERR\",success);
  }
}
```
Comment:
```
Runs the test case.
```
---
id: 325

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
id: 326

Code snippet:
```
@Override public boolean equals(Object o){
  if (!(o instanceof Separator)) {
    return false;
  }
  if (this == o) {
    return true;
  }
  Separator other=(Separator)o;
  return (this.character == other.character && this.quote == other.quote && this.escape == other.escape);
}
```
Comment:
```
Compares this string to the specified object. The result is <code>true</code> if and only if the argument is not <code>null</code> and is a <code>String</code> object that represents the same sequence of characters as this object.
```
---
id: 327

Code snippet:
```
public synchronized void abandon(ConversationAbandonedEvent details){
  if (!abandoned) {
    abandoned=true;
    currentPrompt=null;
    context.getForWhom().abandonConversation(this);
    for (    ConversationAbandonedListener listener : abandonedListeners) {
      listener.conversationAbandoned(details);
    }
  }
}
```
Comment:
```
Abandons and resets the current conversation. Restores the user\'s normal chat behavior.
```
---
id: 328

Code snippet:
```
public Observable<InputStream> open(DriveId driveId){
  return open(driveId,null);
}
```
Comment:
```
Creates a new instance of this class.
```
---
id: 329

Code snippet:
```
public static boolean removeDir(File dir){
  String[] list=dir.list();
  if (list != null) {
    int count=list.length;
    for (int i=0; i < count; i++) {
      String fileName=list[i];
      File file=new File(dir,fileName);
      if (file.isDirectory()) {
        removeDir(file);
      }
 else       if (!file.delete()) {
        Debug.log(\"FileUtils.removeDir() Unable to delete file: \" + file.getAbsolutePath());
      }
    }
  }
  boolean status=dir.delete();
  if (!status) {
    Debug.log(\"FileUtils.removeDir() Unable to delete directory: \" + dir.getAbsolutePath());
  }
  return status;
}
```
Comment:
```
Removes a directory recursively.
```
---
id: 330

Code snippet:
```
public SequenceInputStream(InputStream s1,InputStream s2){
  Vector<InputStream> v=new Vector<>(2);
  v.addElement(s1);
  v.addElement(s2);
  e=v.elements();
  try {
    nextStream();
  }
 catch (  IOException ex) {
    throw new Error(\"panic\");
  }
}
```
Comment:
```
Creates a new instance.
```
---
id: 331

Code snippet:
```
void shutdown(){
  if (isShuttingDown.compareAndSet(false,true)) {
    logsReplicaDB.clear();
    logsCNIndexDB.clear();
  }
}
```
Comment:
```
Shuts down the server.
```
---
id: 332

Code snippet:
```
public Object[] toArray(){
  return al.toArray();
}
```
Comment:
```
Returns an array containing all of the elements in this queue, in proper sequence. <p>The returned array will be \"safe\" in that no references to it are maintained by this queue.  (In other words, this method must allocate a new array).  The caller is thus free to modify the returned array. <p>This method acts as bridge between array-based and collection-based APIs.
```
---
id: 333

Code snippet:
```
public void handleButton3Request(RequestInvocationEvent event){
  forwardToAuthDomainView(event);
}
```
Comment:
```
Handles cancel request.
```
---
id: 334

Code snippet:
```
private static boolean isBeforeDot(String src,int index){
  int ch;
  int cc;
  int len=src.length();
  for (int i=index + Character.charCount(src.codePointAt(index)); i < len; i+=Character.charCount(ch)) {
    ch=src.codePointAt(i);
    if (ch == \'\u0307\') {
      return true;
    }
 else {
      cc=Normalizer.getCombiningClass(ch);
      if ((cc == 0) || (cc == COMBINING_CLASS_ABOVE)) {
        return false;
      }
    }
  }
  return false;
}
```
Comment:
```
Implements the \"Before_Dot\" condition Specification: C is followed by <code>U+0307 COMBINING DOT ABOVE</code>. Any sequence of characters with a combining class that is neither 0 nor 230 may intervene between the current character and the combining dot above. Regular Expression: After C: ([{cc!=230}&{cc!=0}])*[\u0307]
```
---
id: 335

Code snippet:
```
protected Class<?> findLoadedClass0(String name){
  String path=binaryNameToPath(name,true);
  ResourceEntry entry=resourceEntries.get(path);
  if (entry != null) {
    return entry.loadedClass;
  }
  return null;
}
```
Comment:
```
Finds the class with the given name if it has previously been loaded and cached by this class loader, and return the Class object. If this class has not been cached, return <code>null</code>.
```
---
id: 336

Code snippet:
```
private void resetMnemonics(){
  if (mnemonicToIndexMap != null) {
    mnemonicToIndexMap.clear();
    mnemonicInputMap.clear();
  }
}
```
Comment:
```
Resets the map.
```
---
id: 337

Code snippet:
```
public static void addDefaultProfile(SpringApplication app){
  Map<String,Object> defProperties=new HashMap<>();
  defProperties.put(SPRING_PROFILE_DEFAULT,Constants.SPRING_PROFILE_DEVELOPMENT);
  app.setDefaultProperties(defProperties);
}
```
Comment:
```
Add a plugin to the map.
```
---
id: 338

Code snippet:
```
public static void writeJSONString(Map map,Writer out) throws IOException {
  if (map == null) {
    out.write(\"null\");
    return;
  }
  boolean first=true;
  Iterator iter=map.entrySet().iterator();
  out.write(\'{\');
  while (iter.hasNext()) {
    if (first)     first=false;
 else     out.write(\',\');
    Map.Entry entry=(Map.Entry)iter.next();
    out.write(\'\\"\');
    out.write(escape(String.valueOf(entry.getKey())));
    out.write(\'\\"\');
    out.write(\':\');
    JSONValue.writeJSONString(entry.getValue(),out);
  }
  out.write(\'}\');
}
```
Comment:
```
Encode a map into JSON text and write it to out. If this map is also a JSONAware or JSONStreamAware, JSONAware or JSONStreamAware specific behaviours will be ignored at this top level.
```
---
id: 339

Code snippet:
```
public final void testGetX(){
  DSAPrivateKeySpec dpks=new DSAPrivateKeySpec(new BigInteger(\"1\"),new BigInteger(\"2\"),new BigInteger(\"3\"),new BigInteger(\"4\"));
  assertEquals(1,dpks.getX().intValue());
}
```
Comment:
```
getX() test
```
---
id: 340

Code snippet:
```
public static SocketAddress findFreeSocketAddress(){
  try (ServerSocket serverLdapSocket=bindFreePort()){
    return serverLdapSocket.getLocalSocketAddress();
  }
 catch (  IOException e) {
    throw new RuntimeException(e);
  }
}
```
Comment:
```
Finds a free server socket port on the local host.
```
---
id: 341

Code snippet:
```
public void testReceive_BlockNoServerNull() throws Exception {
  assertTrue(this.channel1.isBlocking());
  receiveNoServerNull();
}
```
Comment:
```
Test method for \'DatagramChannelImpl.receive(ByteBuffer)\'
```
---
id: 342

Code snippet:
```
private static void encode(int tag,int length,StringBuilder buffer){
  if (tag == PATTERN_ISO_ZONE && length >= 4) {
    throw new IllegalArgumentException(\"invalid ISO 8601 format: length=\" + length);
  }
  if (length < 255) {
    buffer.append((char)(tag << 8 | length));
  }
 else {
    buffer.append((char)((tag << 8) | 0xff));
    buffer.append((char)(length >>> 16));
    buffer.append((char)(length & 0xffff));
  }
}
```
Comment:
```
Encodes a byte array into Base64 notation.
```
---
id: 343

Code snippet:
```
public void printStackTrace(PrintWriter s){
  super.printStackTrace(s);
}
```
Comment:
```
Prints this <code>NoSuchMechanismException</code>, its backtrace and the cause\'s backtrace to the specified print writer.
```
---
id: 344

Code snippet:
```
boolean isMarker(){
  return value == this;
}
```
Comment:
```
Returns true if this node is a marker. This method isn\'t actually called in any current code checking for markers because callers will have already read value field and need to use that read (not another done here) and so directly test if value points to node.
```
---
id: 345

Code snippet:
```
public boolean isGetAllReturnAttributesEnabled(){
  return getAllAttributesEnabled;
}
```
Comment:
```
Method to check if the boolean getAllAttributesEnabled is enabled or disabled.
```
---
id: 346

Code snippet:
```
private static boolean isAfterSoftDotted(String src,int index){
  int ch;
  int cc;
  for (int i=index; i > 0; i-=Character.charCount(ch)) {
    ch=src.codePointBefore(i);
    if (isSoftDotted(ch)) {
      return true;
    }
 else {
      cc=Normalizer.getCombiningClass(ch);
      if ((cc == 0) || (cc == COMBINING_CLASS_ABOVE)) {
        return false;
      }
    }
  }
  return false;
}
```
Comment:
```
Implements the \"After_Soft_Dotted\" condition Specification: The last preceding character with combining class of zero before C was Soft_Dotted, and there is no intervening combining character class 230 (ABOVE). Regular Expression: Before C: [{Soft_Dotted==true}]([{cc!=230}&{cc!=0}])
```
---
id: 347

Code snippet:
```
public boolean isVerbose(){
  return (environment.get(CLIConstants.ARGUMENT_VERBOSE) != null);
}
```
Comment:
```
Returns true of the CLI has verbose set.
```
---
id: 348

Code snippet:
```
public Object clone(){
  SimpleTimeCondition theClone=null;
  try {
    theClone=(SimpleTimeCondition)super.clone();
  }
 catch (  CloneNotSupportedException e) {
    throw new InternalError();
  }
  if (startDate != null) {
    theClone.startDate=new int[startDate.length];
    System.arraycopy(startDate,0,theClone.startDate,0,startDate.length);
  }
  if (endDate != null) {
    theClone.endDate=new int[endDate.length];
    System.arraycopy(endDate,0,theClone.endDate,0,endDate.length);
  }
  if (enforcementTimeZone != null) {
    theClone.enforcementTimeZone=(TimeZone)enforcementTimeZone.clone();
  }
  if (properties != null) {
    theClone.properties=new HashMap();
    Iterator it=properties.keySet().iterator();
    while (it.hasNext()) {
      Object o=it.next();
      Set values=new HashSet();
      values.addAll((Set)properties.get(o));
      theClone.properties.put(o,values);
    }
  }
  return theClone;
}
```
Comment:
```
Returns a copy of this object.
```
---
id: 349

Code snippet:
```
protected final DTMAxisIterator resetPosition(){
  _position=0;
  return this;
}
```
Comment:
```
Reset the position to zero. NOTE that this does not change the iteration state, only the position number associated with that state. %REVIEW% Document when this would be used?
```
---
id: 350

Code snippet:
```
public static ComponentUI createUI(JComponent c){
  return new SynthLabelUI();
}
```
Comment:
```
Returns the LabelUI implementation used for the skins look and feel.
```
---
id: 351

Code snippet:
```
public boolean isMultiline(){
  return getFieldFlag(FF_MULTILINE);
}
```
Comment:
```
If true, the field can contain multiple lines of text; if false, the field\'s text is restricted to a single line.
```
---
id: 352

Code snippet:
```
public HostNameParser(LexerCore lexer){
  this.lexer=lexer;
  lexer.selectLexer(\"charLexer\");
}
```
Comment:
```
The lexer is initialized with the buffer.
```
---
id: 353

Code snippet:
```
public RoleUnresolvedList(int initialCapacity){
  super(initialCapacity);
}
```
Comment:
```
Constructs an empty RoleUnresolvedList with the initial capacity specified.
```
---
id: 354

Code snippet:
```
public void testPosNegFirstShorter(){
  byte aBytes[]={-2,-3,-4,-4,5,14,23,39,48,57,66,5,14,23};
  byte bBytes[]={-128,9,56,100,-2,-76,89,45,91,3,-15,35,26,-117,23,87,-25,-75};
  int aSign=1;
  int bSign=-1;
  byte rBytes[]={-1,127,-10,-57,-101,-1,-1,-2,-2,-91,-2,31,-1,-11,125,-22,-83,30,95};
  BigInteger aNumber=new BigInteger(aSign,aBytes);
  BigInteger bNumber=new BigInteger(bSign,bBytes);
  BigInteger result=aNumber.or(bNumber);
  byte resBytes[]=new byte[rBytes.length];
  resBytes=result.toByteArray();
  for (int i=0; i < resBytes.length; i++) {
    assertTrue(resBytes[i] == rBytes[i]);
  }
  assertEquals(\"incorrect sign\",-1,result.signum());
}
```
Comment:
```
Or for a positive and a negative number; the first is shorter
```
---
id: 355

Code snippet:
```
@Override public boolean markSupported(){
  return markSupported;
}
```
Comment:
```
Indicates whether this reader is ready to be read.
```
---
id: 356

Code snippet:
```
XSLTAttributeDef(String namespace,String name,boolean required,boolean supportsAVT,boolean prefixedQNameValAllowed,int errorType,String k1,int v1,String k2,int v2){
  this.m_namespace=namespace;
  this.m_name=name;
  this.m_type=prefixedQNameValAllowed ? this.T_ENUM_OR_PQNAME : this.T_ENUM;
  this.m_required=required;
  this.m_supportsAVT=supportsAVT;
  this.m_errorType=errorType;
  m_enums=new StringToIntTable(2);
  m_enums.put(k1,v1);
  m_enums.put(k2,v2);
}
```
Comment:
```
Construct an instance of XSLTElementDef.
```
---
id: 357

Code snippet:
```
public boolean equals(Object obj){
  if (obj instanceof CommandEnvironment) {
    CommandEnvironment env=(CommandEnvironment)obj;
    return ((command == null ? env.command == null : command.equals(env.command)) && Arrays.equals(options,env.options));
  }
 else {
    return false;
  }
}
```
Comment:
```
Compares two command environments for content equality.
```
---
id: 358

Code snippet:
```
public RestAuthException(int responseStatus,Throwable throwable){
  super(throwable);
  statusCode=responseStatus;
}
```
Comment:
```
Constructs a new exception with the specified detail message. The cause is not initialized.
```
---
id: 359

Code snippet:
```
@Override public String toString(){
  return currencyCode;
}
```
Comment:
```
Returns a string representation of this object.
```
---
id: 360

Code snippet:
```
public static PropertyException propertyIsReadOnlyException(final PropertyDefinition<?> pd){
  return new PropertyException(pd,ERR_PROPERTY_IS_READ_ONLY_EXCEPTION.get(pd.getName()));
}
```
Comment:
```
Creates a new instance of this class.
```
---
id: 361

Code snippet:
```
private EnumEvalResult evalComplex(EnumEvalResult left,EnumEvalResult right){
  if (booleanType == EnumBooleanTypes.AND_BOOLEAN_TYPE) {
    if (left == EnumEvalResult.TRUE && right == EnumEvalResult.TRUE) {
      return EnumEvalResult.TRUE;
    }
  }
 else   if (left == EnumEvalResult.TRUE || right == EnumEvalResult.TRUE) {
    return EnumEvalResult.TRUE;
  }
  return EnumEvalResult.FALSE;
}
```
Comment:
```
Returns the result of interpreting the object as an instance of \'<em>Function </em>\'. <!-- begin-user-doc --> This implementation returns null; returning a non-null result will terminate the switch. <!-- end-user-doc -->
```
---
id: 362

Code snippet:
```
public boolean isShort(STypeDef requiredType,NumberLiteral literal,LineCol lineCol) throws SyntaxException {
  return (requiredType == null || requiredType instanceof ShortTypeDef || requiredType instanceof SClassDef && requiredType.isAssignableFrom(getTypeWithName(\"java.lang.Short\",lineCol))) && !literal.literal().contains(\".\");
}
```
Comment:
```
check whether the literal is short type
```
---
id: 363

Code snippet:
```
public String toString(){
  return name;
}
```
Comment:
```
Returns a string representation of this DTD.
```
---
id: 364

Code snippet:
```
public TransportNotSupportedException(String message){
  super(message);
}
```
Comment:
```
Constructs a new exception with the specified detail message. The cause is not initialized.
```
---
id: 365

Code snippet:
```
public ByteArrayBuilder appendIntUTF8(int i){
  return appendString(Integer.toString(i));
}
```
Comment:
```
Append an int to this ByteArrayBuilder by converting it to a String then encoding that string to a UTF-8 byte array.
```
---
id: 366

Code snippet:
```
public int popInt(){
  BaseTypeWrapper wrapper=(BaseTypeWrapper)this.pop();
  Integer value=(Integer)wrapper.getValue();
  return value.intValue();
}
```
Comment:
```
Pop a int.
```
---
id: 367

Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(nodeinsertbeforenomodificationallowederrEE.class,args);
}
```
Comment:
```
Runs this test from the command line.
```
---
id: 368

Code snippet:
```
@Deprecated public static <A>ImmutableList<A> fill(final int len,final A init){
  ImmutableList<A> l=empty();
  for (int i=0; i < len; i++) {
    l=new ImmutableList<>(init,l);
  }
  return l;
}
```
Comment:
```
Returns an immutable list containing the given elements, in order.
```
---
id: 369

Code snippet:
```
protected void endTag(boolean omitted){
  handleText(stack.tag);
  if (omitted && !stack.elem.omitEnd()) {
    error(\"end.missing\",stack.elem.getName());
  }
 else   if (!stack.terminate()) {
    error(\"end.unexpected\",stack.elem.getName());
  }
  handleEndTag(stack.tag);
  stack=stack.next;
  recent=(stack != null) ? stack.elem : null;
}
```
Comment:
```
Handle an end tag. The end tag is popped from the tag stack.
```
---
id: 370

Code snippet:
```
public ConnectionEntryReader search(SearchRequest request){
  addControls(request);
  return conn.getConnection().search(request);
}
```
Comment:
```
Returns the index of the first occurrence of the specified element in this list, or -1 if the list does not contain the element.
```
---
id: 371

Code snippet:
```
public static SetPropSubCommandHandler create(SubCommandArgumentParser parser,ManagedObjectPath<?,?> path,OptionalRelationDefinition<?,?> r) throws ArgumentException {
  return new SetPropSubCommandHandler(parser,path.child(r),r);
}
```
Comment:
```
Creates a new set-xxx-prop sub-command for an optional relation.
```
---
id: 372

Code snippet:
```
String convertNumberToI18N(String numericText){
  if (zeroDigit == \'0\') {
    return numericText;
  }
  int diff=zeroDigit - \'0\';
  char[] array=numericText.toCharArray();
  for (int i=0; i < array.length; i++) {
    array[i]=(char)(array[i] + diff);
  }
  return new String(array);
}
```
Comment:
```
Converts the input numeric text to the internationalized form using the zero character.
```
---
id: 373

Code snippet:
```
private void advance(Node prev){
  Node r, b;
  if ((r=lastRet) != null && !r.isMatched())   lastPred=r;
 else   if ((b=lastPred) == null || b.isMatched())   lastPred=null;
 else {
    Node s, n;
    while ((s=b.next) != null && s != b && s.isMatched() && (n=s.next) != null && n != s)     b.casNext(s,n);
  }
  this.lastRet=prev;
  for (Node p=prev, s, n; ; ) {
    s=(p == null) ? head : p.next;
    if (s == null)     break;
 else     if (s == p) {
      p=null;
      continue;
    }
    Object item=s.item;
    if (s.isData) {
      if (item != null && item != s) {
        nextItem=LinkedTransferQueue.<E>cast(item);
        nextNode=s;
        return;
      }
    }
 else     if (item == null)     break;
    if (p == null)     p=s;
 else     if ((n=s.next) == null)     break;
 else     if (s == n)     p=null;
 else     p.casNext(s,n);
  }
  nextNode=null;
  nextItem=null;
}
```
Comment:
```
Moves to next node after prev, or first node if prev null.
```
---
id: 374

Code snippet:
```
protected boolean includeAuthorityInRequestLine(){
  return connection == null ? policy.usingProxy() : connection.getRoute().getProxy().type() == Proxy.Type.HTTP;
}
```
Comment:
```
Returns true if the request line should contain the full URL with host and port (like \"GET http://android.com/foo HTTP/1.1\") or only the path (like \"GET /foo HTTP/1.1\"). <p>This is non-final because for HTTPS it\'s never necessary to supply the full URL, even if a proxy is in use.
```
---
id: 375

Code snippet:
```
public JsonValue build(){
  return new JsonValue(content);
}
```
Comment:
```
Returns a new builder.
```
---
id: 376

Code snippet:
```
public boolean isError(){
  return ((errorMsg != null) && (errorMsg.length() > 0));
}
```
Comment:
```
Returns <code>true</code> if there is an error while processing request.
```
---
id: 377

Code snippet:
```
public void paintRootPaneBorder(SynthContext context,Graphics g,int x,int y,int w,int h){
  paintBorder(context,g,x,y,w,h,null);
}
```
Comment:
```
Paints the background of a tool bar.
```
---
id: 378

Code snippet:
```
public ServletSecurityElement(HttpConstraintElement httpConstraintElement){
  this(httpConstraintElement,null);
}
```
Comment:
```
Use specified HttpConstraintElement.
```
---
id: 379

Code snippet:
```
public void addJKTableColumn(String keyLabel){
  JKTableColumn col=new JKTableColumn();
  col.setName(keyLabel);
  addJKTableColumn(col);
}
```
Comment:
```
Adds a column to the table.
```
---
id: 380

Code snippet:
```
public static synchronized SSLClientSessionCache usingDirectory(File directory) throws IOException {
  FileClientSessionCache.Impl cache=caches.get(directory);
  if (cache == null) {
    cache=new FileClientSessionCache.Impl(directory);
    caches.put(directory,cache);
  }
  return cache;
}
```
Comment:
```
Returns a cache backed by the given directory. Creates the directory (including parent directories) if necessary. This cache should have exclusive access to the given directory.
```
---
id: 381

Code snippet:
```
public String jmxSslPassword(){
  return values.jmxSslPassword;
}
```
Comment:
```
JMX ssl password.
```
---
id: 382

Code snippet:
```
public void removeBeanContextServicesListener(BeanContextServicesListener bcsl){
  if (bcsl == null)   throw new NullPointerException(\"bcsl\");
synchronized (bcsListeners) {
    if (!bcsListeners.contains(bcsl))     return;
 else     bcsListeners.remove(bcsl);
  }
}
```
Comment:
```
remove a BeanContextServicesListener
```
---
id: 383

Code snippet:
```
public TransformerFactoryConfigurationError(Exception e){
  super(e.toString());
  this.exception=e;
}
```
Comment:
```
Create a new <code>TransformerFactoryConfigurationError</code> with a given <code>Exception</code> base cause of the error.
```
---
id: 384

Code snippet:
```
public final boolean isErrorEnabled(){
  return isLevelEnabled(SimpleLog.LOG_LEVEL_ERROR);
}
```
Comment:
```
<p> Are error messages currently enabled? </p> <p> This allows expensive operations such as <code>String</code> concatenation to be avoided when the message will be ignored by the logger. </p>
```
---
id: 385

Code snippet:
```
public RedisSessionRequestWrapper(HttpServletRequest request){
  super(request);
  this.request=request;
  this.token=request.getHeader(TOKEN_HEADER_NAME);
}
```
Comment:
```
Constructs a new exception with the specified detail message. The cause is not initialized.
```
---
id: 386

Code snippet:
```
public Object[] toArray(){
  fullyLock();
  try {
    int size=count.get();
    Object[] a=new Object[size];
    int k=0;
    for (Node<E> p=head.next; p != null; p=p.next)     a[k++]=p.item;
    return a;
  }
  finally {
    fullyUnlock();
  }
}
```
Comment:
```
Returns an array containing all of the elements in this queue, in proper sequence. <p>The returned array will be \"safe\" in that no references to it are maintained by this queue.  (In other words, this method must allocate a new array).  The caller is thus free to modify the returned array. <p>This method acts as bridge between array-based and collection-based APIs.
```
---
id: 387

Code snippet:
```
public com.sun.identity.saml2.jaxb.entityconfig.SPSSOConfigElement createSPSSOConfigElement() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.saml2.jaxb.entityconfig.impl.SPSSOConfigElementImpl();
}
```
Comment:
```
Create an instance of SPSSOConfigElement
```
---
id: 388

Code snippet:
```
@Override public synchronized String toString(){
  if (elementCount == 0) {
    return \"[]\";
  }
  int length=elementCount - 1;
  StringBuilder buffer=new StringBuilder(elementCount * 16);
  buffer.append(\'[\');
  for (int i=0; i < length; i++) {
    if (elementData[i] == this) {
      buffer.append(\"(this Collection)\");
    }
 else {
      buffer.append(elementData[i]);
    }
    buffer.append(\", \");
  }
  if (elementData[length] == this) {
    buffer.append(\"(this Collection)\");
  }
 else {
    buffer.append(elementData[length]);
  }
  buffer.append(\']\');
  return buffer.toString();
}
```
Comment:
```
Returns the string representation of this vector.
```
---
id: 389

Code snippet:
```
public void paintPanelBackground(SynthContext context,Graphics g,int x,int y,int w,int h){
}
```
Comment:
```
Paints the background of a panel.
```
---
id: 390

Code snippet:
```
public boolean isNodeRelated(DefaultMutableTreeNode aNode){
  return (aNode != null) && (getRoot() == aNode.getRoot());
}
```
Comment:
```
Returns <code>true</code> if the given node is a leaf node.
```
---
id: 391

Code snippet:
```
public LDAPControl(String oid,boolean isCritical){
  super(oid,isCritical);
}
```
Comment:
```
Creates a new LDAP control with the specified OID and criticality.  It will not have a value.
```
---
id: 392

Code snippet:
```
public final boolean removeElement(int s){
  for (int i=0; i < m_firstFree; i++) {
    if (m_map[i] == s) {
      if ((i + 1) < m_firstFree)       System.arraycopy(m_map,i + 1,m_map,i - 1,m_firstFree - i);
 else       m_map[i]=java.lang.Integer.MIN_VALUE;
      m_firstFree--;
      return true;
    }
  }
  return false;
}
```
Comment:
```
Removes the first occurrence of the argument from this vector. If the object is found in this vector, each component in the vector with an index greater or equal to the object\'s index is shifted downward to have an index one smaller than the value it had previously.
```
---
id: 393

Code snippet:
```
public static ArrayList<String> matches(String text,int results){
  ArrayList<String> urls=new ArrayList<String>();
  String[] splitString=(text.split(\" \"));
  for (  String string : splitString) {
    try {
      URL item=new URL(string);
      urls.add(item.toString());
    }
 catch (    Exception e) {
    }
    if (results == FIRST && urls.size() > 0)     break;
  }
  return urls;
}
```
Comment:
```
Convert a string to a URL
```
---
id: 394

Code snippet:
```
public void start(){
}
```
Comment:
```
This method is called by the <code>fixture</code> when the user clicks on the map.
```
---
id: 395

Code snippet:
```
public void addVetoableChangeListener(String name,VetoableChangeListener vcl){
  vcSupport.addVetoableChangeListener(name,vcl);
}
```
Comment:
```
Adds a property change listener.
```
---
id: 396

Code snippet:
```
public boolean isMember(SSOToken token) throws SSOException {
  return (SSOTokenManager.getInstance().isValidToken(token));
}
```
Comment:
```
Determines if the user belongs to  the <code>AuthenticatedUsers</code> object.
```
---
id: 397

Code snippet:
```
public void testEqualsObject(){
  byte aBytes[]={12,56,100,-2,-76,89,45,91,3,-15,35,26,3,91};
  int aSign=1;
  BigInteger aNumber=new BigInteger(aSign,aBytes);
  Object obj=new Object();
  assertFalse(aNumber.equals(obj));
}
```
Comment:
```
equals(Object obj). obj is not a BigInteger
```
---
id: 398

Code snippet:
```
@BeforeTest(groups={\"cli-realm\"}) public void suiteSetup() throws CLIException {
  Map<String,Object> env=new HashMap<String,Object>();
  env.put(CLIConstants.SYS_PROPERTY_COMMAND_NAME,\"amadm\");
  env.put(CLIConstants.SYS_PROPERTY_DEFINITION_FILES,\"com.sun.identity.cli.AccessManager\");
  env.put(CLIConstants.SYS_PROPERTY_OUTPUT_WRITER,outputWriter);
  cmdManager=new CommandManager(env);
}
```
Comment:
```
Create the CLIManager.
```
---
id: 399

Code snippet:
```
public RemoteSession(HttpSession session){
  super();
  debug=Debug.getInstance(\"remoteSession\");
  this.session=(HttpSession)session;
  creationTime=session.getCreationTime();
  id=session.getId();
  lastAccessedTime=session.getLastAccessedTime();
  maxInactiveInterval=session.getMaxInactiveInterval();
  isNew=session.isNew();
  internalAttributes=new HashMap();
  Enumeration aNames=getAttributeNames();
  while (aNames.hasMoreElements()) {
    String attributeName=(String)aNames.nextElement();
    if (isSerializable(getAttribute(attributeName)) && !attributeName.equals(\"LoginCallbacks\") && !attributeName.equals(\"AuthContext\")) {
      internalAttributes.put(attributeName,getAttribute(attributeName));
      internalAttributeNames.add(attributeName);
      debug.message(\"adding attr=\" + attributeName + \", \"+ getAttribute(attributeName));
    }
  }
}
```
Comment:
```
Construct a new session facade. This class wraps the standard HttpSession object allowing it to become serializable.
```
---
