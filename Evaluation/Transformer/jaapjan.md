id: 100

Code snippet:
```
@Override public void close(){
  if (importConfig.invokeImportPlugins()) {
    pluginConfigManager.invokeLDIFImportEndPlugins(importConfig);
  }
  importConfig.close();
}
```
Comment:
```
This method is called by the <code>Application</code>.
```
---
id: 101

Code snippet:
```
public com.sun.identity.liberty.ws.common.jaxb.ps.ExtensionElement createExtensionElement() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.liberty.ws.common.jaxb.ps.impl.ExtensionElementImpl();
}
```
Comment:
```
<!-- begin-user-doc --> <!-- end-user-doc -->
```
---
id: 102

Code snippet:
```
protected void notifyRowSetChanged() throws SQLException {
  checkforRowSetInterface();
  if (listeners.isEmpty() == false) {
    RowSetEvent event=new RowSetEvent((RowSet)this);
    for (    RowSetListener rsl : listeners) {
      rsl.rowSetChanged(event);
    }
  }
}
```
Comment:
```
Notifies all of the listeners registered with this <code>RowSet</code> object that its entire contents have changed. <P> When an application calls methods that change the entire contents of the <code>RowSet</code> object, such as the <code>CachedRowSet</code> methods <code>execute</code>, <code>populate</code>, <code>restoreOriginal</code>, or <code>release</code>, that method calls <code>notifyRowSetChanged</code> internally (either directly or indirectly). An application <b>should</b> never invoke this method directly.
```
---
id: 103

Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(namednodemapsetnameditemns10.class,args);
}
```
Comment:
```
Runs this test from the command line.
```
---
id: 104

Code snippet:
```
public void addSigners(SignerInformationStore signerStore){
  Iterator it=signerStore.getSigners().iterator();
  while (it.hasNext()) {
    _signers.add(it.next());
  }
}
```
Comment:
```
Add a store of precalculated signers to the generator.
```
---
id: 105

Code snippet:
```
public int hashCode(){
  int hash=0;
  for (int i=0; i < rdns.size(); i++) {
    Rdn rdn=rdns.get(i);
    hash+=rdn.hashCode();
  }
  return hash;
}
```
Comment:
```
Returns a hash code for this instance.
```
---
id: 106

Code snippet:
```
private SynthStyle mergeStyles(List styles){
  int size=styles.size();
  if (size == 0) {
    return null;
  }
 else   if (size == 1) {
    return (SynthStyle)((DefaultSynthStyle)styles.get(0)).clone();
  }
  DefaultSynthStyle style=(DefaultSynthStyle)styles.get(size - 1);
  style=(DefaultSynthStyle)style.clone();
  for (int counter=size - 2; counter >= 0; counter--) {
    style=((DefaultSynthStyle)styles.get(counter)).addTo(style);
  }
  return style;
}
```
Comment:
```
Returns a copy of this style.
```
---
id: 107

Code snippet:
```
public String toString(){
  StringBuffer buffer=new StringBuffer();
  buffer.append(\"<wst:RequestSecurityTokenResponse \" + \"xmlns:wst=\\"http://schemas.xmlsoap.org/ws/2005/02/trust\\">\").append(token.toString()).append(\"<wsp:AppliesTo \").append(\"xmlns:wsp=\\"http://schemas.xmlsoap.org/ws/2004/09/policy\\">\").append(\"<wsa:EndpointReference xmlns:\").append(\"wsa=\\"http://schemas.xmlsoap.org/ws/2004/08/addressing\\">\").append(\"<wsa:Address>\" + appliesTo + \"</wsa:Address>\").append(\"</wsa:EndpointReference>\").append(\"</wsp:AppliesTo>\").append(\"</wst:RequestSecurityTokenResponse>\");
  return buffer.toString();
}
```
Comment:
```
toString methode: creates a String representation of the object
```
---
id: 108

Code snippet:
```
public static void unbindThread(Object obj,Object token){
  if (ContextAccessController.checkSecurityToken(obj,token)) {
    threadBindings.remove(Thread.currentThread());
    threadObjectBindings.remove(Thread.currentThread());
  }
}
```
Comment:
```
Unbinds a thread and a naming context.
```
---
id: 109

Code snippet:
```
public E remove(){
  return removeFirst();
}
```
Comment:
```
Retrieves and removes the head (first element) of this list.
```
---
id: 110

Code snippet:
```
public long insert(Long ruleID,Long actionID){
  if (ruleID == null || actionID == null) {
    throw new IllegalArgumentException(\"insert parameter null.\");
  }
  ContentValues initialValues=new ContentValues();
  initialValues.put(KEY_RULEID,ruleID);
  initialValues.put(KEY_ACTIONID,actionID);
  return database.insert(DATABASE_TABLE,null,initialValues);
}
```
Comment:
```
Insert a new RuleAction record
```
---
id: 111

Code snippet:
```
public void resetDebug(String mf){
  getDebugServiceInstance().resetDebug(mf);
}
```
Comment:
```
Method reset
```
---
id: 112

Code snippet:
```
public static Long[] transformLongArray(long[] source){
  Long[] destin=new Long[source.length];
  for (int i=0; i < source.length; i++) {
    destin[i]=source[i];
  }
  return destin;
}
```
Comment:
```
convert Integer array to int array
```
---
id: 113

Code snippet:
```
public int previous(){
  return this.icuIterator.previous();
}
```
Comment:
```
Obtains the previous collation element in the source string.
```
---
id: 114

Code snippet:
```
public ClientCredentials(final String clientId,final char[] clientSecret,final boolean isAuthenticated,final boolean basicAuth){
  this.clientId=clientId;
  this.clientSecret=clientSecret;
  this.isAuthenticated=isAuthenticated;
  this.basicAuth=basicAuth;
}
```
Comment:
```
Constructs a new ClientCredentials instance.
```
---
id: 115

Code snippet:
```
private static boolean commonNeedIncrement(int roundingMode,int qsign,int cmpFracHalf,boolean oddQuot){
switch (roundingMode) {
case ROUND_UNNECESSARY:
    throw new ArithmeticException(\"Rounding necessary\");
case ROUND_UP:
  return true;
case ROUND_DOWN:
return false;
case ROUND_CEILING:
return qsign > 0;
case ROUND_FLOOR:
return qsign < 0;
default :
assert roundingMode >= ROUND_HALF_UP && roundingMode <= ROUND_HALF_EVEN : \"Unexpected rounding mode\" + RoundingMode.valueOf(roundingMode);
if (cmpFracHalf < 0) return false;
 else if (cmpFracHalf > 0) return true;
 else {
assert cmpFracHalf == 0;
switch (roundingMode) {
case ROUND_HALF_DOWN:
return false;
case ROUND_HALF_UP:
return true;
case ROUND_HALF_EVEN:
return oddQuot;
default :
throw new AssertionError(\"Unexpected rounding mode\" + roundingMode);
}
}
}
}
```
Comment:
```
Returns true if the given state is currently active otherwise false.
```
---
id: 116

Code snippet:
```
public void mouseReleased(MouseEvent e){
  if (!e.isConsumed() && shouldHandleRelease && SwingUtilities.isLeftMouseButton(e)) {
    adjustCaretAndFocus(e);
  }
}
```
Comment:
```
Called when the mouse is released.
```
---
id: 117

Code snippet:
```
public void updateUI(){
  setUI((MenuBarUI)UIManager.getUI(this));
}
```
Comment:
```
This method is called when the user presses the \"hide\" button.
```
---
id: 118

Code snippet:
```
public AddResponseProtocolOp(int resultCode,LocalizableMessage errorMessage){
  this.resultCode=resultCode;
  this.errorMessage=errorMessage;
}
```
Comment:
```
Constructs a new instance of this class.
```
---
id: 119

Code snippet:
```
protected int drawSelectedText(Graphics g,int x,int y,int p0,int p1) throws BadLocationException {
  g.setColor(selected);
  Container c=getContainer();
  if (c instanceof JPasswordField) {
    JPasswordField f=(JPasswordField)c;
    if (!f.echoCharIsSet()) {
      return super.drawSelectedText(g,x,y,p0,p1);
    }
    char echoChar=f.getEchoChar();
    int n=p1 - p0;
    for (int i=0; i < n; i++) {
      x=drawEchoCharacter(g,x,y,echoChar);
    }
  }
  return x;
}
```
Comment:
```
Draws the given text.
```
---
id: 120

Code snippet:
```
private NameIDInfo(){
}
```
Comment:
```
Private contstructor.
```
---
id: 121

Code snippet:
```
public void printTagContent(PrintWriter aWriter,String tag,String content) throws Exception {
  aWriter.print(\"<\");
  aWriter.print(tag);
  aWriter.print(\">\");
  aWriter.print(convertStr(content));
  aWriter.print(\"</\");
  aWriter.print(tag);
  aWriter.println(\">\");
}
```
Comment:
```
Print the value from tag as content.
```
---
id: 122

Code snippet:
```
private Node<K,V> findPredecessorOfLast(){
  for (; ; ) {
    Index<K,V> q=head;
    for (; ; ) {
      Index<K,V> d, r;
      if ((r=q.right) != null) {
        if (r.indexesDeletedNode()) {
          q.unlink(r);
          break;
        }
        if (r.node.next != null) {
          q=r;
          continue;
        }
      }
      if ((d=q.down) != null)       q=d;
 else       return q.node;
    }
  }
}
```
Comment:
```
Specialized variant of findPredecessor to get predecessor of last valid node.  Needed when removing the last entry.  It is possible that all successors of returned node will have been deleted upon return, in which case this method can be retried.
```
---
id: 123

Code snippet:
```
private void clearRegistryForComponent(WXComponent component){
  WXComponent removedComponent=mRegistry.remove(component.getDomObject().ref);
  if (removedComponent != null) {
    removedComponent.removeAllEvent();
    removedComponent.removeStickyStyle();
  }
  if (component instanceof WXVContainer) {
    WXVContainer container=(WXVContainer)component;
    int count=container.childCount();
    for (int i=count - 1; i >= 0; --i) {
      clearRegistryForComponent(container.getChild(i));
    }
  }
}
```
Comment:
```
This method was generated by MyBatis Generator. This method corresponds to the database table notification
```
---
id: 124

Code snippet:
```
private void removeEntryFromIndexes(IndexBuffer buffer,Entry entry,EntryID entryID) throws StorageRuntimeException, DirectoryException {
  for (  AttributeIndex index : attrIndexMap.values()) {
    index.removeEntry(buffer,entryID,entry);
  }
  for (  VLVIndex vlvIndex : vlvIndexMap.values()) {
    vlvIndex.removeEntry(buffer,entryID,entry);
  }
}
```
Comment:
```
Removes the specified key from the cache if it exists.
```
---
id: 125

Code snippet:
```
String popImportURL(){
  return (String)m_importStack.pop();
}
```
Comment:
```
Pop an import href from the stylesheet stack.
```
---
id: 126

Code snippet:
```
private String convertIntToIntString(int quoteParam){
  String quoteParamString=(new Integer(quoteParam)).toString();
  return quoteParamString;
}
```
Comment:
```
convertIntToIntString - private method to convert Integer to Integer String
```
---
id: 127

Code snippet:
```
public static boolean matchPassword(String plain,JKUser user){
  return JKEncDec.encode(plain).equals(user.getPassword());
}
```
Comment:
```
Returns true if the user has a valid email address.
```
---
id: 128

Code snippet:
```
@Deprecated public String encode(String path){
  return encode(path,\"UTF-8\");
}
```
Comment:
```
URL encodes the provided path using UTF-8.
```
---
id: 129

Code snippet:
```
protected Control(Type type){
  this.type=type;
}
```
Comment:
```
Constructs a Control with the specified type.
```
---
id: 130

Code snippet:
```
public StyledTextAction(String nm){
  super(nm);
}
```
Comment:
```
Creates a new StyledTextAction from a string action name.
```
---
id: 131

Code snippet:
```
public SerialRef(Ref ref) throws SerialException, SQLException {
  if (ref == null) {
    throw new SQLException(\"Cannot instantiate a SerialRef object \" + \"with a null Ref object\");
  }
  reference=ref;
  object=ref;
  if (ref.getBaseTypeName() == null) {
    throw new SQLException(\"Cannot instantiate a SerialRef object \" + \"that returns a null base type name\");
  }
 else {
    baseTypeName=ref.getBaseTypeName();
  }
}
```
Comment:
```
Constructs a <code>SerialRef</code> object from the given <code>Ref</code> object.
```
---
id: 132

Code snippet:
```
public String toString(final boolean deep){
  final StringBuffer buf=new StringBuffer();
  if (deep) {
    buf.append(getPriviligeId());
    buf.append(\",\");
  }
  buf.append(getNumber());
  buf.append(\" : \");
  buf.append(getFullName());
  if (deep && this.childs.size() > 0) {
    buf.append(this.childs.toString());
  }
  return buf.toString();
}
```
Comment:
```
To string.
```
---
id: 133

Code snippet:
```
public HashPrintJobAttributeSet(PrintJobAttributeSet attributes){
  super(attributes,PrintJobAttribute.class);
}
```
Comment:
```
Construct a new attribute set, initially populated with the values from the  given set where the members of the attribute set are restricted to the <code>PrintJobAttribute</code> interface.
```
---
id: 134

Code snippet:
```
public boolean equals(Object o){
  if (o == this) {
    return true;
  }
  if (o instanceof TabSet) {
    TabSet ts=(TabSet)o;
    int count=getTabCount();
    if (ts.getTabCount() != count) {
      return false;
    }
    for (int i=0; i < count; i++) {
      TabStop ts1=getTab(i);
      TabStop ts2=ts.getTab(i);
      if ((ts1 == null && ts2 != null) || (ts1 != null && !getTab(i).equals(ts.getTab(i)))) {
        return false;
      }
    }
    return true;
  }
  return false;
}
```
Comment:
```
Indicates whether this <code>TabSet</code> is equal to another one.
```
---
id: 135

Code snippet:
```
public void push(final long value){
  if (value == 0L || value == 1L) {
    mv.visitInsn(Opcodes.LCONST_0 + (int)value);
  }
 else {
    mv.visitLdcInsn(value);
  }
}
```
Comment:
```
Generates the instruction to push the given value on the stack.
```
---
id: 136

Code snippet:
```
private static void checkNotNull(Object v){
  if (v == null)   throw new NullPointerException();
}
```
Comment:
```
Throws NullPointerException if argument is null.
```
---
id: 137

Code snippet:
```
public static <R,A,B>Future<R> chain(A input,Function<A,Future<B>> operation1,Function<B,Future<R>> operation2){
  Future<R> future=Future.future();
  operation1.apply(input).setHandler(null);
  return future;
}
```
Comment:
```
Creates a new instance of this class.
```
---
id: 138

Code snippet:
```
public boolean is_leaf(){
  return children.isEmpty();
}
```
Comment:
```
Returns <code>true</code>.
```
---
id: 139

Code snippet:
```
public com.sun.identity.liberty.ws.idpp.jaxb.ModifyType.ModificationType createModifyTypeModificationType() throws javax.xml.bind.JAXBException {
  return new com.sun.identity.liberty.ws.idpp.jaxb.impl.ModifyTypeImpl.ModificationTypeImpl();
}
```
Comment:
```
Create an instance of ModifyTypeModificationType
```
---
id: 140

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
Ensures that the list of messages is at least the given number of messages.
```
---
id: 141

Code snippet:
```
protected void fireStateChanged(){
  Object[] listeners=listenerList.getListenerList();
  for (int i=listeners.length - 2; i >= 0; i-=2) {
    if (listeners[i] == ChangeListener.class) {
      if (changeEvent == null) {
        changeEvent=new ChangeEvent(this);
      }
      ((ChangeListener)listeners[i + 1]).stateChanged(changeEvent);
    }
  }
}
```
Comment:
```
Notifies all listeners that have registered interest for notification on this event type.  The event instance is lazily created using the parameters passed into the fire method.
```
---
id: 142

Code snippet:
```
public org.omg.DynamicAny.DynAny current_component() throws org.omg.DynamicAny.DynAnyPackage.TypeMismatch {
  org.omg.CORBA.portable.ServantObject $so=_servant_preinvoke(\"current_component\",_opsClass);
  DynEnumOperations $self=(DynEnumOperations)$so.servant;
  try {
    return $self.current_component();
  }
  finally {
    _servant_postinvoke($so);
  }
}
```
Comment:
```
<!-- begin-user-doc --> <!-- end-user-doc -->
```
---
id: 143

Code snippet:
```
public Schema readSchema() throws DirectoryException, ConfigException, InitializationException {
  SchemaHandler schemaHandler=serverContext.getSchemaHandler();
  final File schemaDir=schemaHandler.getSchemaDirectoryPath();
  final List<String> fileNames=StaticUtils.getFileNames(SchemaUtils.getSchemaFiles(schemaDir));
  Schema baseSchema=getBaseSchema();
  SchemaBuilder schemaBuilder=new SchemaBuilder(baseSchema);
  for (  String schemaFile : fileNames) {
    schemaHandler.loadSchemaFileIntoSchemaBuilder(new File(schemaDir,schemaFile),schemaBuilder,baseSchema);
  }
  return buildSchema(schemaBuilder);
}
```
Comment:
```
Reads the configuration file.
```
---
id: 144

Code snippet:
```
public void testNegPosFirstLonger(){
  String numA=\"-2837462783428374767845648748973847593874837948575684767\";
  String numB=\"293478573489347658763745839457637\";
  String res=\"-2837462783428374767845615168483972194300564226167553532\";
  BigInteger aNumber=new BigInteger(numA);
  BigInteger bNumber=new BigInteger(numB);
  BigInteger result=aNumber.xor(bNumber);
  assertTrue(res.equals(result.toString()));
}
```
Comment:
```
Xor for two positive numbers; the first is longer
```
---
id: 145

Code snippet:
```
public void dispose(){
  for (  GuiSubWindowSavable cur_subwindow : permanent_subwindows)   cur_subwindow.dispose();
  permanent_subwindows.clear();
  for (  GuiSubWindowTemp curr_subwindow : temporary_subwindows)   curr_subwindow.board_frame_disposed();
  temporary_subwindows.clear();
  board_panel.itera_board.dispose();
  work_frame.dispose();
}
```
Comment:
```
Actions to be taken when this frame vanishes.
```
---
id: 146

Code snippet:
```
public static IOFileFilter asFileFilter(FileFilter filter){
  return new DelegateFileFilter(filter);
}
```
Comment:
```
Returns a filter that accepts the given filter.
```
---
id: 147

Code snippet:
```
public void doPost(HttpServletRequest request,HttpServletResponse response) throws ServletException, IOException {
  doGetPost(request,response);
}
```
Comment:
```
Handles the HTTP POST request.
```
---
id: 148

Code snippet:
```
public void insert_wstring(String value) throws org.omg.DynamicAny.DynAnyPackage.TypeMismatch, org.omg.DynamicAny.DynAnyPackage.InvalidValue {
  org.omg.CORBA.portable.ServantObject $so=_servant_preinvoke(\"insert_wstring\",_opsClass);
  DynStructOperations $self=(DynStructOperations)$so.servant;
  try {
    $self.insert_wstring(value);
  }
  finally {
    _servant_postinvoke($so);
  }
}
```
Comment:
```
Rename an object.
```
---
id: 149

Code snippet:
```
public DefaultPooledObject(final T object){
  this.object=object;
}
```
Comment:
```
Create a new instance that wraps the provided object so that the pool can track the state of the pooled object.
```
---
id: 150

Code snippet:
```
public HttpException(final String message){
  super(message);
}
```
Comment:
```
Creates a new HttpException with the specified detail message.
```
---
id: 151

Code snippet:
```
public void notify_changed(BrdItem p_item){
}
```
Comment:
```
Notify the observers, that they can synchronize the changes on p_object.
```
---
id: 152

Code snippet:
```
public void skippedEntity(String name) throws SAXException {
  if (DEBUG)   System.out.println(\"TransformerHandlerImpl#skippedEntity: \" + name);
  if (m_contentHandler != null) {
    m_contentHandler.skippedEntity(name);
  }
}
```
Comment:
```
Filter a skipped entity event.
```
---
id: 153

Code snippet:
```
Object processNUMBER(StylesheetHandler handler,String uri,String name,String rawName,String value,ElemTemplateElement owner) throws org.xml.sax.SAXException {
  if (getSupportsAVT()) {
    Double val;
    AVT avt=null;
    try {
      avt=new AVT(handler,uri,name,rawName,value,owner);
      if (avt.isSimple()) {
        val=Double.valueOf(value);
      }
    }
 catch (    TransformerException te) {
      throw new org.xml.sax.SAXException(te);
    }
catch (    NumberFormatException nfe) {
      handleError(handler,XSLTErrorResources.INVALID_NUMBER,new Object[]{name,value},nfe);
      return null;
    }
    return avt;
  }
 else {
    try {
      return Double.valueOf(value);
    }
 catch (    NumberFormatException nfe) {
      handleError(handler,XSLTErrorResources.INVALID_NUMBER,new Object[]{name,value},nfe);
      return null;
    }
  }
}
```
Comment:
```
Process an attribute string of type T_NUMBER into a double value.
```
---
id: 154

Code snippet:
```
public void closeAllSubpaths(){
  for (  Subpath subpath : subpaths) {
    subpath.setClosed(true);
  }
}
```
Comment:
```
Closes all subpathes contained in this path.
```
---
id: 155

Code snippet:
```
public boolean passed(){
  return getSkippedTestCases().isEmpty() && getFailedTestCases().isEmpty();
}
```
Comment:
```
Gets the value of the usetable property.
```
---
id: 156

Code snippet:
```
public void uninstallUI(JComponent c){
  uninstallKeyboardActions();
  uninstallListeners();
  uninstallDefaults();
  dividerLocationIsSet=false;
  dividerKeyboardResize=false;
  splitPane=null;
}
```
Comment:
```
Invokes the <code>uninstallUI</code> method on each UI handled by this object.
```
---
id: 157

Code snippet:
```
public boolean isConfigured(){
  return AMSetupServlet.isConfigured(baseDir);
}
```
Comment:
```
Gets the value of the enabled property.
```
---
id: 158

Code snippet:
```
public LockFactory(){
  lockCache=new WeakHashMap<Key<K>,Reference<Lock>>();
}
```
Comment:
```
Constructs a new LockFactory instance.
```
---
id: 159

Code snippet:
```
@Override public void init() throws ServletException {
  registry=Registry.getRegistry(null,null);
  mBeanServer=Registry.getRegistry(null,null).getMBeanServer();
}
```
Comment:
```
Initialize this servlet.
```
---
id: 160

Code snippet:
```
public NSNumber(int i){
  doubleValue=longValue=i;
  type=INTEGER;
}
```
Comment:
```
Creates an integer number.
```
---
id: 161

Code snippet:
```
public R visitIPAddressMask(IPAddressMaskPropertyDefinition pd,AddressMask v,P p){
  return visitUnknown(pd,v,p);
}
```
Comment:
```
Visit a IP address mask.
```
---
id: 162

Code snippet:
```
public AMInvalidDNException(String msg,String errorCode){
  super(msg,errorCode);
}
```
Comment:
```
Constructs a new <code>AMException</code> with detailed message.
```
---
id: 163

Code snippet:
```
public void testConstrStringWithExponentWithoutPoint2(){
  String a=\"-238768787678287e-214\";
  int aScale=214;
  BigInteger bA=new BigInteger(\"-238768787678287\");
  BigDecimal aNumber=new BigDecimal(a);
  assertEquals(\"incorrect value\",bA,aNumber.unscaledValue());
  assertEquals(\"incorrect scale\",aScale,aNumber.scale());
}
```
Comment:
```
new BigDecimal(String value); value contains exponent and does not contain decimal point
```
---
id: 164

Code snippet:
```
public ObjectStreamField(String name,Class<?> cl){
  if (name == null) {
    throw new NullPointerException(\"name == null\");
  }
 else   if (cl == null) {
    throw new NullPointerException(\"cl == null\");
  }
  this.name=name;
  this.type=new WeakReference<Class<?>>(cl);
}
```
Comment:
```
Creates a new instance of this class.
```
---
id: 165

Code snippet:
```
public static void main(final String[] args){
  DOMTestCase.doMain(nodesetprefix05.class,args);
}
```
Comment:
```
Runs this test from the command line.
```
---
id: 166

Code snippet:
```
StringVector processPREFIX_LIST(StylesheetHandler handler,String uri,String name,String rawName,String value) throws org.xml.sax.SAXException {
  StringTokenizer tokenizer=new StringTokenizer(value,\" \t
\r\f\");
  int nStrings=tokenizer.countTokens();
  StringVector strings=new StringVector(nStrings);
  for (int i=0; i < nStrings; i++) {
    String prefix=tokenizer.nextToken();
    String url=handler.getNamespaceForPrefix(prefix);
    if (prefix.equals(Constants.ATTRVAL_DEFAULT_PREFIX) || url != null)     strings.addElement(prefix);
 else     throw new org.xml.sax.SAXException(XSLMessages.createMessage(XSLTErrorResources.ER_CANT_RESOLVE_NSPREFIX,new Object[]{prefix}));
  }
  return strings;
}
```
Comment:
```
Process an attribute string of type T_CHAR into a String value.
```
---
id: 167

Code snippet:
```
private Map<String,Set<String>> attributesToMap(Attribute[] attributes){
  Map<String,Set<String>> result=new HashMap<>();
  for (  Attribute attribute : attributes) {
    result.put(attribute.getName(),new HashSet<>(Arrays.asList(attribute.getValues())));
  }
  return result;
}
```
Comment:
```
Convert attributes into a map.
```
---
id: 168

Code snippet:
```
protected boolean isServiced(String name) throws Exception {
  String[] params={name};
  String[] signature={\"java.lang.String\"};
  Boolean result=(Boolean)mBeanServer.invoke(oname,\"isServiced\",params,signature);
  return result.booleanValue();
}
```
Comment:
```
Returns true if the user is authenticated.
```
---
id: 169

Code snippet:
```
private ZoneOffsetTransition[] findTransitionArray(int year){
  Integer yearObj=year;
  ZoneOffsetTransition[] transArray=lastRulesCache.get(yearObj);
  if (transArray != null) {
    return transArray;
  }
  ZoneOffsetTransitionRule[] ruleArray=lastRules;
  transArray=new ZoneOffsetTransition[ruleArray.length];
  for (int i=0; i < ruleArray.length; i++) {
    transArray[i]=ruleArray[i].createTransition(year);
  }
  if (year < LAST_CACHED_YEAR) {
    lastRulesCache.putIfAbsent(yearObj,transArray);
  }
  return transArray;
}
```
Comment:
```
Creates a new transition.
```
---
id: 170

Code snippet:
```
public static boolean isValidPhone(String phone){
  boolean isValidPhone=false;
  Pattern pattern=Pattern.compile(\"^((13[0-9])|(17[^4,\\D])|(15[^4,\\D])|(18[0-9]))\\d{8}$\");
  isValidPhone=pattern.matcher(phone).matches();
  return isValidPhone;
}
```
Comment:
```
Checks if the given string is a valid email address.
```
---
id: 171

Code snippet:
```
protected void fireTreeNodesChanged(Object source,Object[] path,int[] childIndices,Object[] children){
  Object[] listeners=listenerList.getListenerList();
  TreeModelEvent e=null;
  for (int i=listeners.length - 2; i >= 0; i-=2) {
    if (listeners[i] == TreeModelListener.class) {
      if (e == null)       e=new TreeModelEvent(source,path,childIndices,children);
      ((TreeModelListener)listeners[i + 1]).treeNodesChanged(e);
    }
  }
}
```
Comment:
```
Notifies all listeners that have registered interest for notification on this event type.  The event instance  is lazily created using the parameters passed into  the fire method.
```
---
id: 172

Code snippet:
```
private void refreshStationUI(int station){
  mTextStationValue.setText(FmRadioUtils.formatStation(station));
  if (FmRadioStation.isFavoriteStation(mContext,station)) {
    mButtonAddToFavorite.setImageResource(R.drawable.btn_fm_favorite_on_selector);
    mTextStationName.setText(FmRadioStation.getStationName(mContext,station,FmRadioStation.STATION_TYPE_FAVORITE));
  }
 else {
    mButtonAddToFavorite.setImageResource(R.drawable.btn_fm_favorite_off_selector);
    mTextStationName.setText(\"\");
  }
}
```
Comment:
```
Refresh the favorite button with the given station, if the station is favorite station, show favorite icon, else show non-favorite icon.
```
---
id: 173

Code snippet:
```
public String toXML(){
  StringBuilder stringBuilder=new StringBuilder();
  return stringBuilder.toString();
}
```
Comment:
```
Default toXML Method to Marshal Object into XML.
```
---
id: 174

Code snippet:
```
public NoSuchAlgorithmException(String msg){
  super(msg);
}
```
Comment:
```
Constructs a NoSuchAlgorithmException with the specified detail message. A detail message is a String that describes this particular exception, which may, for example, specify which algorithm is not available.
```
---
id: 175

Code snippet:
```
public Object parse(String s) throws XMLException {
  ByteArrayInputStream bin=null;
  String st=stripWhitespaces(s);
  try {
    bin=new ByteArrayInputStream(st.getBytes(\"UTF-8\"));
  }
 catch (  UnsupportedEncodingException ex) {
    throw new XMLException(\"Encoding not supported:\" + ex.toString());
  }
  return parse(bin);
}
```
Comment:
```
Parses an XML document from a String variable.
```
---
id: 176

Code snippet:
```
public CharHolder(){
}
```
Comment:
```
Constructs a new <code>AttributedCharacterIterator</code>.
```
---
id: 177

Code snippet:
```
public ValidationException(String message,Throwable exception){
  this(message,null,exception);
}
```
Comment:
```
Constructs a new exception with the specified detail message, cause, and bean for JAX-WS exception serialization.
```
---
id: 178

Code snippet:
```
@Override public void destroySubcontext(String name) throws NamingException {
  destroySubcontext(new CompositeName(name));
}
```
Comment:
```
Unregisters a listener.
```
---
id: 179

Code snippet:
```
public void readLabel(String readLabelFile) throws Exception {
  BufferedReader trUsers=new BufferedReader(new InputStreamReader(new FileInputStream(readLabelFile)));
  String line=\"\";
  while ((line=trUsers.readLine()) != null) {
    String[] strs=line.split(\"\t\");
    labels[Integer.valueOf(strs[0])]=Integer.valueOf(strs[1]);
  }
  trUsers.close();
}
```
Comment:
```
Read in category file of different source.
```
---
id: 180

Code snippet:
```
@Override public void flush() throws IOException {
  super.flush();
}
```
Comment:
```
Flushes this stream to ensure all pending data is sent out to the target stream. This implementation then also flushes the target stream.
```
---
id: 181

Code snippet:
```
public OrganizationAlreadyExistsException(String msg){
  super(msg);
}
```
Comment:
```
Constructs a new exception with the specified detail message. The cause is not initialized.
```
---
id: 182

Code snippet:
```
public SQLPermission(String name,String actions){
  super(name,actions);
}
```
Comment:
```
Creates a new <code>SQLPermission</code> object with the specified name. The name is the symbolic name of the <code>SQLPermission</code>; the actions <code>String</code> is currently unused and should be <code>null</code>.
```
---
id: 183

Code snippet:
```
public void appendToFsb(org.apache.xml.utils.FastStringBuffer fsb){
  XString xstring=(XString)xstr();
  xstring.appendToFsb(fsb);
}
```
Comment:
```
<p>Append to the <code>toString</code> an <code>int</code> value.</p>
```
---
id: 184

Code snippet:
```
public boolean isSSOTokenValid(){
  try {
    SMSEntry.validateToken(token);
    return true;
  }
 catch (  SMSException smse) {
    debug.warning(\"ServiceSchemaManager: token is not valid.\",smse);
  }
  return false;
}
```
Comment:
```
Returns true if admin token  cached within this class is valid
```
---
id: 185

Code snippet:
```
protected final boolean isListState(){
  return stateTextTypes.charAt(state) == \'L\';
}
```
Comment:
```
Returns true if the fragment is currently active.
```
---
id: 186

Code snippet:
```
public long insert(long timeStamp,long logEventID,String ruleName,String actionAppName,String actionEventName,String actionParameters,String description){
  if (ruleName == null || actionAppName == null || actionEventName == null || actionParameters == null || description == null) {
    throw new IllegalArgumentException(\"insert parameter null.\");
  }
  ContentValues initialValues=new ContentValues();
  initialValues.put(KEY_TIMESTAMP,timeStamp);
  initialValues.put(KEY_LOGEVENTID,logEventID);
  initialValues.put(KEY_RULENAME,ruleName);
  initialValues.put(KEY_ACTIONAPPNAME,actionAppName);
  initialValues.put(KEY_ACTIONEVENTNAME,actionEventName);
  initialValues.put(KEY_ACTIONPARAMETERS,actionParameters);
  initialValues.put(KEY_DESCRIPTION,description);
  return database.insert(DATABASE_TABLE,null,initialValues);
}
```
Comment:
```
Insert a new Action Log record.
```
---
id: 187

Code snippet:
```
@Override public void delete(){
  cachedContent=null;
  File outputFile=getStoreLocation();
  if (outputFile != null && outputFile.exists()) {
    outputFile.delete();
  }
}
```
Comment:
```
Closes the cache and deletes all of its stored values. This will delete all files in the cache directory including files that weren\'t created by the cache.
```
---
id: 188

Code snippet:
```
public boolean hasBinaryAttributes(){
  return false;
}
```
Comment:
```
Returns whether it has the value.
```
---
id: 189

Code snippet:
```
private void updateBaseConfig(BaseConfigType baseConfig,Map values,String role) throws AMConsoleException {
  List attrList=baseConfig.getAttribute();
  if (role.equals(EntityModel.IDENTITY_PROVIDER)) {
    attrList.clear();
    baseConfig=createAttributeElement(getIDPEXDataMap(),baseConfig);
    attrList=baseConfig.getAttribute();
  }
 else   if (role.equals(EntityModel.SERVICE_PROVIDER)) {
    attrList.clear();
    baseConfig=createAttributeElement(getSPEXDataMap(),baseConfig);
    attrList=baseConfig.getAttribute();
  }
  for (Iterator it=attrList.iterator(); it.hasNext(); ) {
    AttributeElement avpnew=(AttributeElement)it.next();
    String name=avpnew.getName();
    if (values.keySet().contains(name)) {
      Set set=(Set)values.get(name);
      if (set != null) {
        avpnew.getValue().clear();
        avpnew.getValue().addAll(set);
      }
    }
  }
}
```
Comment:
```
Updates the BaseConfig Object with the map of values passed.
```
---
id: 190

Code snippet:
```
Pair<Boolean,Record<K,V>> positionToKey(final long blockStartPosition,final K key,final KeyMatchingStrategy matchStrategy,final PositionStrategy positionStrategy) throws ChangelogException {
  Record<K,V> record=readRecord(blockStartPosition);
  Record<K,V> previousRecord=null;
  long previousPosition=blockStartPosition;
  while (record != null) {
    final int keysComparison=record.getKey().compareTo(key);
    if ((keysComparison == 0 && matchStrategy == EQUAL_TO_KEY) || (keysComparison >= 0 && matchStrategy != EQUAL_TO_KEY)) {
      return getMatchingRecord(matchStrategy,positionStrategy,keysComparison,record,previousRecord,previousPosition);
    }
    previousRecord=record;
    previousPosition=getFilePosition();
    record=readRecord();
  }
  if (matchStrategy == LESS_THAN_OR_EQUAL_TO_KEY) {
    return getRecordNoMatchForLessStrategy(positionStrategy,previousRecord,previousPosition);
  }
  return Pair.of(false,null);
}
```
Comment:
```
Position before, at or after provided key, starting from provided block start position and reading until key is found according to matching and positioning strategies.
```
---
id: 191

Code snippet:
```
public PageRanges(int lowerBound,int upperBound){
  super(lowerBound,upperBound);
  if (lowerBound > upperBound) {
    throw new IllegalArgumentException(\"Null range specified\");
  }
 else   if (lowerBound < 1) {
    throw new IllegalArgumentException(\"Page value < 1 specified\");
  }
}
```
Comment:
```
Creates a new instance.
```
---
id: 192

Code snippet:
```
public HashPrintJobAttributeSet(){
  super(PrintJobAttribute.class);
}
```
Comment:
```
Construct a new, empty hash print job attribute set.
```
---
id: 193

Code snippet:
```
protected void uninstallListeners(){
  if (propertyChangeListener != null) {
    splitPane.removePropertyChangeListener(propertyChangeListener);
    propertyChangeListener=null;
  }
  if (focusListener != null) {
    splitPane.removeFocusListener(focusListener);
    focusListener=null;
  }
  keyboardUpLeftListener=null;
  keyboardDownRightListener=null;
  keyboardHomeListener=null;
  keyboardEndListener=null;
  keyboardResizeToggleListener=null;
  handler=null;
}
```
Comment:
```
Uninstalls the event listeners for the UI.
```
---
id: 194

Code snippet:
```
public boolean isValid(SigningHandler signingHandler){
  if (isSignatureValid == null) {
    isSignatureValid=jwt.verify(signingHandler);
  }
  return isSignatureValid && isContentValid();
}
```
Comment:
```
Verifies that the JWT is valid by: <ul> <li>verifying the signature</li> <li>ensuring the JWT contains the \'iss\', \'sub\', \'aud\' and \'exp\' claims</li> <li>ensuring the JWT expiry is not unreasonably far in the future</li> <li>ensuring the JWT has not expired</li> <li>ensuring the JWT is not being used before its \'not before time\'</li> <li>ensuring the JWT issued at time is not unreasonably far in the past</li> </ul>
```
---
id: 195

Code snippet:
```
@Override public boolean ready() throws IOException {
synchronized (lock) {
    checkNotClosed();
    return ((end - pos) > 0) || in.ready();
  }
}
```
Comment:
```
Indicates whether this reader is ready to be read without blocking.
```
---
id: 196

Code snippet:
```
public void startElement(String uri,String localName,String qName,Attributes attributes) throws SAXException {
}
```
Comment:
```
Receive notification of the start of an element. <p>By default, do nothing.  Application writers may override this method in a subclass to take specific actions at the start of each element (such as allocating a new tree node or writing output to a file).</p>
```
---
id: 197

Code snippet:
```
public boolean visitFunction(ExpressionOwner owner,Function func){
  if (func instanceof FuncExtFunction) {
    String namespace=((FuncExtFunction)func).getNamespace();
    m_sroot.getExtensionNamespacesManager().registerExtension(namespace);
  }
 else   if (func instanceof FuncExtFunctionAvailable) {
    String arg=((FuncExtFunctionAvailable)func).getArg0().toString();
    if (arg.indexOf(\":\") > 0) {
      String prefix=arg.substring(0,arg.indexOf(\":\"));
      String namespace=this.m_sroot.getNamespaceForPrefix(prefix);
      m_sroot.getExtensionNamespacesManager().registerExtension(namespace);
    }
  }
  return true;
}
```
Comment:
```
Visits the given type-specific AST node. <p> The default implementation does nothing and return true. Subclasses may reimplement. </p>
```
---
id: 198

Code snippet:
```
private boolean isAgent(AMIdentity amIdentityUser){
  boolean isAgent=false;
  try {
    if (amIdentityUser != null && amIdentityUser.getType().equals(IdType.AGENT)) {
      isAgent=true;
      DEBUG.message(\"user is of type \'Agent\'\");
    }
  }
 catch (  Exception e) {
    if (DEBUG.messageEnabled()) {
      DEBUG.message(\"Error isAgent : \" + e.toString());
    }
  }
  return isAgent;
}
```
Comment:
```
Returns <code>true</code> if the logged in user is \'Agent\'.
```
---
id: 199

Code snippet:
```
public boolean beginTblSearchGroupDisplay(ChildDisplayEvent event){
  return !is2dot2Agent() && !isAgentAuthenticator();
}
```
Comment:
```
Called when the user presses the \"Cancel\" button.
```
---
